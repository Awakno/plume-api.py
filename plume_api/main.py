import requests
from typing import Optional, Dict, Any, Union, Literal


class PlumeAPI:
    BASE_URL = "https://plume.ptarmigan.xyz/api"

    def __init__(self):
        self.user_agent = "PlumeAPI.py/1.0.0"
        self.headers = {"User-Agent": self.user_agent}

    def _get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        response = requests.get(
            f"{self.BASE_URL}{endpoint}", headers=self.headers, params=params
        )
        response.raise_for_status()
        return response.json()

    def _get_file(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> bytes:
        response = requests.get(
            f"{self.BASE_URL}{endpoint}", headers=self.headers, params=params
        )
        response.raise_for_status()
        return response.content

    def _request(
        self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        response = requests.request(
            method, f"{self.BASE_URL}{endpoint}", headers=self.headers, params=params
        )
        response.raise_for_status()
        return response

    # Fun endpoints
    def eight_ball(self, locale: Optional[str] = None) -> Dict[str, Any]:
        return self._get("/8ball", {"locale": locale})

    height_ball = eight_ball  # Alias for deprecated name

    def emoji_mix(self, left: str, right: str) -> Dict[str, Any]:
        return self._get("/emoji-mix", {"left": left, "right": right})

    def fun_fact(self, locale: Optional[str] = None) -> Dict[str, Any]:
        return self._get("/funfact", {"locale": locale})

    def iss_image(self, circle: Optional[bool] = None) -> bytes:
        return self._get_file("/iss-image", {"circle": circle})

    def iss(self) -> Dict[str, Any]:
        return self._get("/iss")

    def joke(self, locale: Optional[str] = None) -> Dict[str, Any]:
        return self._get("/joke", {"locale": locale})

    def math(self, expr: str) -> Dict[str, Any]:
        return self._get("/math", {"expr": expr})

    def meme(self) -> Dict[str, Any]:
        return self._get("/meme")

    def nasa_apod(self) -> Dict[str, Any]:
        return self._get("/nasa-apod")

    def npm(self, name: str) -> Dict[str, Any]:
        return self._get("/npm", {"name": name})

    def quote(self, locale: Optional[str] = None) -> Dict[str, Any]:
        return self._get("/quote", {"locale": locale})

    def random_emoji_mix(self) -> Dict[str, Any]:
        return self._get("/random-emoji-mix")

    def urban(self, word: str) -> Dict[str, Any]:
        return self._get("/urban", {"word": word})

    def color(self, hex: str) -> Dict[str, Any]:
        return self._get("/color", {"hex": hex})

    def color_image(self, hex: str) -> bytes:
        return self._get_file(f"/color/image/{hex}")

    def random_color(self) -> Dict[str, Any]:
        return self._get("/color/random")

    def decode(self, type: str, text: str) -> Dict[str, Any]:
        return self._get(f"/decode/{type}", {"text": text})

    def encode(self, type: str, text: str) -> Dict[str, Any]:
        return self._get(f"/encode/{type}", {"text": text})

    def github_repository(self, name: str) -> Dict[str, Any]:
        return self._get("/github/repository", {"name": name})

    def github_user(self, name: str) -> Dict[str, Any]:
        return self._get("/github/user", {"name": name})

    # Utility endpoints
    def captcha(self) -> Dict[str, Union[str, bytes]]:
        response = self._request("GET", "/captcha")
        code = response.headers.get("X-Captcha-Code")
        if not code:
            raise ValueError("X-Captcha-Code missing in response")
        return {"code": code, "image": response.content}

    def crypto(self, name: str, currency: Literal["usd", "eur"]) -> Dict[str, Any]:
        return self._get("/crypto", {"name": name, "currency": currency})

    def definition(self, locale: str, word: str) -> Dict[str, Any]:
        return self._get("/definition", {"locale": locale, "word": word})

    def exec_code(self, language: str, code: str) -> Dict[str, Any]:
        return self._get("/exec", {"language": language, "code": code})

    def free_games(self, locale: Optional[str] = None) -> Dict[str, Any]:
        return self._get("/free-games", {"locale": locale})

    def ip_info(self, ip: str) -> Dict[str, Any]:
        return self._get("/ipinfo", {"ip": ip})

    def qrcode(self, text: str) -> bytes:
        return self._get_file("/qrcode", {"text": text})

    def reverse_text(self, text: str) -> Dict[str, Any]:
        return self._get("/reverse-text", {"text": text})

    def translate(self, text: str, to: str) -> Dict[str, Any]:
        return self._get("/translate", {"text": text, "to": to})

    def weather(self, city: str) -> Dict[str, Any]:
        return self._get("/weather", {"city": city})

    def wikipedia(self, page: str, locale: Optional[str] = None) -> Dict[str, Any]:
        return self._get("/wikipedia", {"page": page, "locale": locale})

    # Interactions
    def interaction(self, type: str) -> Dict[str, Any]:
        return self._get(f"/interactions/{type}")

    # Image Creation
    def achievement(self, text: str) -> bytes:
        return self._get_file("/images/achievement", {"text": text})

    def alert(self, text: str) -> bytes:
        return self._get_file("/images/alert", {"text": text})

    def caution(self, text: str) -> bytes:
        return self._get_file("/images/caution", {"text": text})

    def challenge(self, text: str) -> bytes:
        return self._get_file("/images/challenge", {"text": text})

    def jail(self, avatar: str) -> bytes:
        return self._get_file("/images/jail", {"avatar": avatar})

    def nokia(self, url: str) -> bytes:
        return self._get_file("/images/nokia", {"url": url})

    def tweet(
        self,
        avatar: str,
        name: str,
        username: str,
        text: str,
        retweets: Optional[int] = None,
        quote_tweets: Optional[int] = None,
        likes: Optional[int] = None,
    ) -> bytes:
        params = {
            "avatar": avatar,
            "name": name,
            "username": username,
            "text": text,
            "retweets": retweets,
            "quote_tweets": quote_tweets,
            "likes": likes,
        }
        return self._get_file("/images/tweet", params)

    def wanted(self, avatar: str) -> bytes:
        return self._get_file("/images/wanted", {"avatar": avatar})

    # Image Manipulation
    def blur(self, url: str) -> bytes:
        return self._get_file("/images/blur", {"url": url})

    def colorify(self, url: str, color: str) -> bytes:
        return self._get_file("/images/colorify", {"url": url, "color": color})

    def grayscale(self, url: str) -> bytes:
        return self._get_file("/images/grayscale", {"url": url})

    def invert(self, url: str) -> bytes:
        return self._get_file("/images/invert", {"url": url})

    def rotate(self, url: str, deg: int) -> bytes:
        return self._get_file("/images/rotate", {"url": url, "deg": deg})

    # Meme Creation
    def change_my_mind(self, text: str) -> bytes:
        return self._get_file("/memes/changemymind", {"text": text})

    def did_you_mean(self, search: str, correction: str) -> bytes:
        return self._get_file(
            "/memes/didyoumean", {"search": search, "correction": correction}
        )

    def drake(self, top: str, bottom: str) -> bytes:
        return self._get_file("/memes/drake", {"top": top, "bottom": bottom})

    def duolingo(self, text: str) -> bytes:
        return self._get_file("/memes/duolingo", {"text": text})

    def facts(self, text: str) -> bytes:
        return self._get_file("/memes/facts", {"text": text})

    def fuze3(self, text: str) -> bytes:
        return self._get_file("/memes/fuze3", {"text": text})

    def hugo(self, text: str) -> bytes:
        return self._get_file("/memes/hugo", {"text": text})

    def nothing(self, text: str) -> bytes:
        return self._get_file("/memes/nothing", {"text": text})

    def oogway(self, text: str) -> bytes:
        return self._get_file("/memes/oogway", {"text": text})

    def sadcat(self, top: str, bottom: str) -> bytes:
        return self._get_file("/memes/sadcat", {"top": top, "bottom": bottom})

    def stonks(self, avatar: str, stonks: Optional[bool] = None) -> bytes:
        return self._get_file("/memes/stonks", {"avatar": avatar, "stonks": stonks})

    def table_flip(self, avatar: str) -> bytes:
        return self._get_file("/memes/tableflip", {"avatar": avatar})

    def water(self, text: str) -> bytes:
        return self._get_file("/memes/water", {"text": text})

    def woosh(self, avatar: str) -> bytes:
        return self._get_file("/memes/woosh", {"avatar": avatar})

    # Cards
    def boost(self, avatar: str, username: str, text: Optional[str] = None) -> bytes:
        return self._get_file(
            "/cards/boost", {"avatar": avatar, "username": username, "text": text}
        )

    def couple(
        self,
        avatar1: str,
        avatar2: str,
        percentage: Optional[int] = None,
        primary_color: Optional[str] = None,
    ) -> bytes:
        params = {
            "avatar1": avatar1,
            "avatar2": avatar2,
            "percentage": percentage,
            "primary_color": primary_color,
        }
        return self._get_file("/cards/couple", params)

    def rank(
        self,
        avatar: str,
        global_name: str,
        username: str,
        level: int,
        xp: int,
        max_xp: int,
        rank: Optional[int] = None,
        bg_url: Optional[str] = None,
        bg_color: Optional[str] = None,
        blur: Optional[bool] = None,
        color: Optional[str] = None,
    ) -> bytes:
        params = {
            "avatar": avatar,
            "global_name": global_name,
            "username": username,
            "level": level,
            "xp": xp,
            "max_xp": max_xp,
            "rank": rank,
            "bg_url": bg_url,
            "bg_color": bg_color,
            "blur": blur,
            "color": color,
        }
        return self._get_file("/cards/rank", params)

    def welcome(
        self,
        avatar: str,
        text1: str,
        text2: Optional[str] = None,
        text3: Optional[str] = None,
        bg_url: Optional[str] = None,
        bg_color: Optional[str] = None,
        font_color: Optional[str] = None,
        blur: Optional[bool] = None,
    ) -> bytes:
        params = {
            "avatar": avatar,
            "text1": text1,
            "text2": text2,
            "text3": text3,
            "bg_url": bg_url,
            "bg_color": bg_color,
            "font_color": font_color,
            "blur": blur,
        }
        return self._get_file("/cards/welcome", params)

    def goodbye(
        self,
        avatar: str,
        text1: str,
        text2: Optional[str] = None,
        text3: Optional[str] = None,
        bg_url: Optional[str] = None,
        bg_color: Optional[str] = None,
        font_color: Optional[str] = None,
        blur: Optional[bool] = None,
    ) -> bytes:
        params = {
            "avatar": avatar,
            "text1": text1,
            "text2": text2,
            "text3": text3,
            "bg_url": bg_url,
            "bg_color": bg_color,
            "font_color": font_color,
            "blur": blur,
        }
        return self._get_file("/cards/goodbye", params)

    def upside_down(self, text: str) -> Dict[str, Any]:
        return self._get("/upside-down", {"text": text})

    def screenshot(self, url: str) -> bytes:
        return self._get_file("/screenshot", {"url": url})

    def pepe_hug(self, avatar: str) -> bytes:
        return self._get_file("/pepe-hug", {"avatar": avatar})
