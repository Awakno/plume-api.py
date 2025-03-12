# PlumeAPI

PlumeAPI is a Python wrapper for the Plume API, providing easy access to various endpoints for fun, utility, and image manipulation.

## Installation

To install PlumeAPI, simply use pip:

```bash
pip install plume_api
```

## Usage

Here's a quick example of how to use the PlumeAPI:

```python
from plume_api import PlumeAPI

api = PlumeAPI()

# Get a random 8-ball response
response = api.eight_ball()
print(response)

# Get a fun fact
fun_fact = api.fun_fact()
print(fun_fact)

# Get an ISS image
iss_image = api.iss_image()
with open('iss_image.png', 'wb') as f:
    f.write(iss_image)
```

## Available Endpoints

### Fun Endpoints

- `eight_ball(locale: Optional[str] = None) -> Dict[str, Any]`
- `emoji_mix(left: str, right: str) -> Dict[str, Any]`
- `fun_fact(locale: Optional[str] = None) -> Dict[str, Any]`
- `iss_image(circle: Optional[bool] = None) -> bytes`
- `iss() -> Dict[str, Any]`
- `joke(locale: Optional[str] = None) -> Dict[str, Any]`
- `math(expr: str) -> Dict[str, Any]`
- `meme() -> Dict[str, Any]`
- `nasa_apod() -> Dict[str, Any]`
- `npm(name: str) -> Dict[str, Any]`
- `quote(locale: Optional[str] = None) -> Dict[str, Any]`
- `random_emoji_mix() -> Dict[str, Any]`
- `urban(word: str) -> Dict[str, Any]`
- `color(hex: str) -> Dict[str, Any]`
- `color_image(hex: str) -> bytes`
- `random_color() -> Dict[str, Any]`
- `decode(type: str, text: str) -> Dict[str, Any]`
- `encode(type: str, text: str) -> Dict[str, Any]`
- `github_repository(name: str) -> Dict[str, Any]`
- `github_user(name: str) -> Dict[str, Any]`
- `upside_down(text: str) -> Dict[str, Any]`

### Utility Endpoints

- `captcha() -> Dict[str, Union[str, bytes]]`
- `crypto(name: str, currency: Literal["usd", "eur"]) -> Dict[str, Any]`
- `definition(locale: str, word: str) -> Dict[str, Any]`
- `exec_code(language: str, code: str) -> Dict[str, Any]`
- `free_games(locale: Optional[str] = None) -> Dict[str, Any]`
- `ip_info(ip: str) -> Dict[str, Any]`
- `qrcode(text: str) -> bytes`
- `reverse_text(text: str) -> Dict[str, Any]`
- `translate(text: str, to: str) -> Dict[str, Any]`
- `weather(city: str) -> Dict[str, Any]`
- `wikipedia(page: str, locale: Optional[str] = None) -> Dict[str, Any]`

### Image Creation

- `achievement(text: str) -> bytes`
- `alert(text: str) -> bytes`
- `caution(text: str) -> bytes`
- `challenge(text: str) -> bytes`
- `jail(avatar: str) -> bytes`
- `nokia(url: str) -> bytes`
- `tweet(avatar: str, name: str, username: str, text: str, retweets: Optional[int] = None, quote_tweets: Optional[int] = None, likes: Optional[int] = None) -> bytes`
- `wanted(avatar: str) -> bytes`
- `screenshot(url: str) -> bytes`

### Image Manipulation

- `blur(url: str) -> bytes`
- `colorify(url: str, color: str) -> bytes`
- `grayscale(url: str) -> bytes`
- `invert(url: str) -> bytes`
- `rotate(url: str, deg: int) -> bytes`

### Meme Creation

- `change_my_mind(text: str) -> bytes`
- `did_you_mean(search: str, correction: str) -> bytes`
- `drake(top: str, bottom: str) -> bytes`
- `duolingo(text: str) -> bytes`
- `facts(text: str) -> bytes`
- `fuze3(text: str) -> bytes`
- `hugo(text: str) -> bytes`
- `nothing(text: str) -> bytes`
- `oogway(text: str) -> bytes`
- `sadcat(top: str, bottom: str) -> bytes`
- `stonks(avatar: str, stonks: Optional[bool] = None) -> bytes`
- `table_flip(avatar: str) -> bytes`
- `water(text: str) -> bytes`
- `woosh(avatar: str) -> bytes`
- `pepe_hug(avatar: str) -> bytes`

### Cards

- `boost(avatar: str, username: str, text: Optional[str] = None) -> bytes`
- `couple(avatar1: str, avatar2: str, percentage: Optional[int] = None, primary_color: Optional[str] = None) -> bytes`
- `rank(avatar: str, global_name: str, username: str, level: int, xp: int, max_xp: int, rank: Optional[int] = None, bg_url: Optional[str] = None, bg_color: Optional[str] = None, blur: Optional[bool] = None, color: Optional[str] = None) -> bytes`
- `welcome(avatar: str, text1: str, text2: Optional[str] = None, text3: Optional[str] = None, bg_url: Optional[str] = None, bg_color: Optional[str] = None, font_color: Optional[str] = None, blur: Optional[bool] = None) -> bytes`
- `goodbye(avatar: str, text1: str, text2: Optional[str] = None, text3: Optional[str] = None, bg_url: Optional[str] = None, bg_color: Optional[str] = None, font_color: Optional[str] = None, blur: Optional[bool] = None) -> bytes`

## License

This project is licensed under the MIT License.