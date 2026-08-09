from datetime import datetime, timezone
from unittest.mock import Mock

from src.models import ContentItem, SourceType
from src.orchestrator import HorizonOrchestrator


_PUBLISHED_AT = datetime(2026, 8, 9, 12, 0, tzinfo=timezone.utc)


def _item(item_id: str, source_type: SourceType) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=source_type,
        title=item_id,
        url=f"https://example.com/{item_id.replace(':', '-')}",
        published_at=_PUBLISHED_AT,
    )


def test_filter_processed_github_releases_keeps_new_items_and_tracks_fetched_ids():
    orchestrator = object.__new__(HorizonOrchestrator)
    orchestrator.processed_release_ids = {"github:release:old"}

    items = [
        _item("github:release:old", SourceType.GITHUB),
        _item("github:release:new", SourceType.GITHUB),
        _item("github:event:42", SourceType.GITHUB),
        _item("rss:item", SourceType.RSS),
    ]

    filtered = orchestrator._filter_processed_releases(items)

    assert [item.id for item in filtered] == [
        "github:release:new",
        "github:event:42",
        "rss:item",
    ]
    assert orchestrator.pending_release_ids == {"github:release:new"}


def test_filter_processed_github_releases_does_not_mark_old_release_again():
    orchestrator = object.__new__(HorizonOrchestrator)
    orchestrator.processed_release_ids = {"github:release:old"}

    orchestrator._filter_processed_releases(
        [_item("github:release:old", SourceType.GITHUB)]
    )

    assert orchestrator.pending_release_ids == set()


def test_save_processed_release_state_merges_pending_ids():
    orchestrator = object.__new__(HorizonOrchestrator)
    orchestrator.processed_release_ids = {"github:release:old"}
    orchestrator.pending_release_ids = {"github:release:new"}
    orchestrator.storage = Mock()

    orchestrator._save_processed_release_state()

    assert orchestrator.processed_release_ids == {
        "github:release:old",
        "github:release:new",
    }
    orchestrator.storage.save_processed_release_ids.assert_called_once_with(
        {"github:release:old", "github:release:new"}
    )
