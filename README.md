CapSolver.com package for Python
=
![PyPI - Wheel](https://img.shields.io/pypi/wheel/capsolver_python?style=plastic) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/capsolver_python?style=flat) ![GitHub last commit](https://img.shields.io/github/last-commit/alperensert/capsolver_python?style=flat) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/alperensert/capsolver_python?style=flat) ![PyPI - Downloads](https://img.shields.io/pypi/dm/capsolver_python?style=flat) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alperensert/capsolver_python?style=flat) ![GitHub Repo stars](https://img.shields.io/github/stars/alperensert/capsolver_python?style=social) 

[CapSolver.com](https://capsolver.com) package for Python3

Register now from [here](https://dashboard.capsolver.com/passport/register?inviteCode=kXa8cbNF-b2l).

If you have any problem with usage, [read the documentation](https://github.com/alperensert/capsolver_python/wiki) or [create an issue](https://github.com/alperensert/capsolver_python/issues/new)

### Installation
```
pip install capsolver_python
```

### Supported captcha types
- Image to Text
- Recaptcha V2
- Recaptcha V2 Enterprise
- Recaptcha V3
- FunCaptcha
- HCaptcha
- GeeTest
- AntiAkamaiBMP
- HCaptcha Classification
- DataDome Slider
- FunCaptcha Classification

Usage examples
-

#### ImageToText

```python
from capsolver_python import ImageToTextTask

capsolver = ImageToTextTask("API_KEY")
task_id = capsolver.create_task(image_path="img.png")
result = capsolver.join_task_result(task_id)
print(result.get("text"))
```

#### Recaptcha v2

```python
from capsolver_python import RecaptchaV2Task

capsolver = RecaptchaV2Task("API_KEY")
task_id = capsolver.create_task("website_url", "website_key")
result = capsolver.join_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```

#### Recaptcha v2 enterprise

```python
from capsolver_python import RecaptchaV2EnterpriseTask

capsolver = RecaptchaV2EnterpriseTask("API_KEY")
task_id = capsolver.create_task("website_url", "website_key", {"s": "payload value"}, "api_domain")
result = capsolver.join_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```

#### GeeTest

```python
from capsolver_python import GeeTestTask

capsolver = GeeTestTask("API_KEY")
task_id = capsolver.create_task("website_url", "gt", "challenge")
result= capsolver.join_task_result(task_id)
print(result.get("challenge"))
print(result.get("seccode"))
print(result.get("validate"))
```

For other examples and api documentation please visit [wiki](https://captchaai.atlassian.net/wiki/spaces/CAPTCHAAI/overview)