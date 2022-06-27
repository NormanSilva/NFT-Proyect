from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from django.db.backends.base.client import BaseDatabaseClient
from django.db.backends.mysql.base import DatabaseWrapper

class DatabaseClient(BaseDatabaseClient):
    connection: DatabaseWrapper
    executable_name: str = ...
    @classmethod
    def settings_to_cmd_args_env(
        cls,
        settings_dict: Dict[str, Any],
        parameters: Iterable[str],
    ) -> Tuple[List[str], Optional[Dict[str, str]]]: ...
