from pydantic import BaseModel

from typing import Optional


class SettingsPayload(BaseModel):
    token: Optional[str]
    chatId: Optional[int]
    notifications: dict

    class Config:
        schema_extra = {
            "example": {
                "token": "5584437396:AAFnY_NQZre654DOAu_BQz654fMLyMXmU",
                "chatId": 5309987774,
                "notifications": {
                    "asset_adjustment_request_processing": {
                        "title": "Asset adjustment request processing",
                        "statuses": {
                            "pending": False,
                            "approved": False,
                            "failed": False,
                            "inquiring": False,
                            "scheduled": False,
                            "revoking": False,
                            "revoked": False,
                        },
                    },
                    "asset_cancel_request_processing": {
                        "title": "Asset cancel request processing",
                        "statuses": {
                            "pending": False,
                            "approved": False,
                            "failed": False,
                            "inquiring": False,
                            "scheduled": False,
                            "revoking": False,
                            "revoked": False,
                        },
                    },
                    "asset_change_request_processing": {
                        "title": "Asset change request processing",
                        "statuses": {
                            "pending": False,
                            "approved": False,
                            "failed": False,
                            "inquiring": False,
                            "scheduled": False,
                            "revoking": False,
                            "revoked": False,
                        },
                    },
                    "asset_purchase_request_processing": {
                        "title": "Asset purchase request processing",
                        "statuses": {
                            "pending": True,
                            "approved": True,
                            "failed": True,
                            "inquiring": True,
                            "scheduled": True,
                            "revoking": True,
                            "revoked": True,
                        },
                    },
                    "asset_resume_request_processing": {
                        "title": "Asset resume request processing",
                        "statuses": {
                            "pending": False,
                            "approved": False,
                            "failed": False,
                            "inquiring": False,
                            "scheduled": False,
                            "revoking": False,
                            "revoked": False,
                        },
                    },
                    "asset_suspend_request_processing": {
                        "title": "Asset suspend request processing",
                        "statuses": {
                            "pending": False,
                            "approved": False,
                            "failed": False,
                            "inquiring": False,
                            "scheduled": False,
                            "revoking": False,
                            "revoked": False,
                        },
                    },
                    "helpdesk_case_processing": {
                        "title": "Helpdesk case processing",
                        "statuses": {
                            "pending": False,
                            "inquiring": False,
                            "resolved": False,
                            "closed": False,
                        },
                    },
                    "installation_status_change": {
                        "title": "Installation status change",
                        "statuses": {
                            "installed": False,
                            "uninstalled": False,
                        },
                    },
                    "part_usage_file_request_processing": {
                        "title": "Part usage file request processing",
                        "statuses": {
                            "draft": False,
                            "ready": False,
                            "closed": False,
                            "failed": False,
                        },
                    },
                    "tier_account_update_request_processing": {
                        "title": "Tier account update request processing",
                        "statuses": {
                            "pending": False,
                            "accepted": False,
                            "ignored": False,
                        },
                    },
                    "tier_config_adjustment_request_processing": {
                        "title": "Tier config adjustment request processing",
                        "statuses": {
                            "pending": False,
                            "approved": False,
                            "failed": False,
                            "inquiring": False,
                        },
                    },
                    "tier_config_change_request_processing": {
                        "title": "Tier config change request processing",
                        "statuses": {
                            "pending": False,
                            "approved": False,
                            "failed": False,
                            "inquiring": False,
                        },
                    },
                    "tier_config_setup_request_processing": {
                        "title": "Tier config setup request processing",
                        "statuses": {
                            "pending": True,
                            "approved": True,
                            "failed": True,
                            "inquiring": False,
                        },
                    },
                    "usage_file_request_processing": {
                        "title": "Usage file request processing",
                        "statuses": {
                            "draft": False,
                            "uploading": False,
                            "uploaded": False,
                            "invalid": False,
                            "processing": False,
                            "processed": False,
                            "ready": False,
                            "rejected": False,
                            "pending": False,
                            "accepted": False,
                            "closed": False,
                        },
                    },
                },
            },
        }


class TestMessagePayload(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    detail: str
