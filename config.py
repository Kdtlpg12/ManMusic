from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "20400887"))
API_HASH = getenv("API_HASH", "535abea1d0cc67a4be1f57de026a846f")
BOT_TOKEN = getenv("BOT_TOKEN", "5854090671:AAGPB9j8HrvKGZciigaBzj56KA7kLkNRa_M")
BOT_NAME = getenv("BOT_NAME","Joox_Musicbot")
BOT_USERNAME = getenv("BOT_USERNAME", "Joox_Musicbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "punyaa_ra")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "idoganz")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
START_IMG = getenv("START_IMG", "")
PING_IMG = getenv("PING_IMG", "")
SESSION_NAME = getenv("SESSION_NAME", "BQB8Lh-BAowOwzIUpdsveyCIG1eSNNefzudcn5R-Op3vDqoInMh_4gj7zncJjDazBCozy8PeomOwOw0V2kp6saUM8vxFrLwevUUchJ3A1WSuJ8Lu-igj0icgoEI8jWN8zxcrIBNci8hQj9JQCS7KPAANiOW2naHIyffQ1H1VgDuR4EAOS2biQLyWhvhhg2FoFJgMIjjnzz65TlSWrYK6Mlx1OpVXPDk8Y1aKhwrKL2evZ1oXNTIGv_ZXwwEAafnwtaDDFzvB9fFqCZH_6WVyoWCEmgGY_Noai3IVvN17bxqV9oBezV7YDyESOTLG74OP4sxvYTMyBel9CHeuMpV1hf3CAAAAAV9_gS8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
