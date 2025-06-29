from server.domain.models.document import Doc
from typing import Optional, Any

class DocumentProcessor:
    async def process(self, file: Any) -> Optional[Doc]:
        pass
