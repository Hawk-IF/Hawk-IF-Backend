from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from hawkBackend.domain.exceptions.validate_exceptions import ValidateException
from hawkBackend.domain.guards import BaseGuard


class BaseEntity:

    _id: UUID
    _is_active: bool
    _created_at: datetime
    _updated_at: datetime
    _created_by: UUID | None
    _updated_by: UUID | None

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @property
    def created_by(self) -> UUID | None:
        return self._created_by

    @property
    def updated_by(self) -> UUID | None:
        return self._updated_by

    @classmethod
    def create(
        cls,
        *,
        is_active: bool = True,
        created_by: UUID | None = None,
        updated_by: UUID | None = None,
    ) -> BaseEntity:

        validator = (
            BaseGuard()
            .validate_is_active(is_active)
            .validate_created_by(created_by)
            .validate_updated_by(updated_by)
        )

        if validator.errors:
            raise ValidateException(validator.errors)

        now = datetime.now(timezone.utc)

        instance = cls()

        instance._id = uuid4()
        instance._is_active = is_active
        instance._created_at = now
        instance._updated_at = now
        instance._created_by = created_by
        instance._updated_by = updated_by

        return instance

    @classmethod
    def reconstruct(
        cls,
        *,
        id: UUID,
        created_at: datetime,
        updated_at: datetime,
        is_active: bool,
        created_by: UUID | None,
        updated_by: UUID | None,
    ) -> BaseEntity:

        instance = cls()

        instance._id = id
        instance._created_at = created_at
        instance._updated_at = updated_at
        instance._is_active = is_active
        instance._created_by = created_by
        instance._updated_by = updated_by

        return instance

    def update(
        self,
        *,
        is_active: bool | None = None,
        updated_by: UUID | None = None,
    ) -> None:

        validator = BaseGuard()

        if is_active is not None:
            validator.validate_is_active(is_active)

        if updated_by is not None:
            validator.validate_updated_by(updated_by)

        if validator.errors:
            raise ValidateException(validator.errors)

        changed = False

        if is_active is not None:
            self._is_active = is_active
            changed = True

        if updated_by is not None:
            self._updated_by = updated_by
            changed = True

        if changed:
            self._updated_at = datetime.now(timezone.utc)
