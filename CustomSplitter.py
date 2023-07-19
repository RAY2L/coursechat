from typing import Any, List

from langchain.text_splitter import TextSplitter


class CustomSplitter(TextSplitter):
    """Implementation of custom text splitter"""

    def __init__(self, **kwargs: Any) -> None:
        """Create a new TextSplitter."""
        super().__init__(**kwargs)

    def split_text(self, text: str) -> List[str]:
        return [text]
