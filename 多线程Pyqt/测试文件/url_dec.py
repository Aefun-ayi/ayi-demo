import requests
import base64


url = "TQCvXCMpbhXWAQfz%2BNjH3MYgTlCwMSLNpeZ86oxlweaR5aMHAm0juTG10n6bUWQLzOrRHRSrFefIReD253DYYuDIEJ1zUvIzvX1sxQfOMo4hm1Eynx%2BEISccg1m4YJrwjssFIOJ0aoPF5NzTqgY23%2BRX9wWL73mRK9WnIXuLE1rKNZPtAJRchYl8%2BOBi6LSRb4A0kNIY6%2BGP%2BxUzoJN9M0%2B0Dqdv2qiwqd9BoevJqgnWWBs52%2B0nI5BPKjJirmDpY6oJaDsIljlqZTRgDnjgxPvTO9TrzzsjX5iMrmSfK3fmraGaEcAtIeKsXQH9x6RYW5kSWQ9NTRkZDg0ZjRiOTFlZTAwYiZhcHBpZD0zOTc3OSZjaGE9dml5eSZpbWVpPTZhNDA0MjMwMzkyMGIwNWM1YTQyMmU5MzMzNzExZTRhMWFkODhmZGFlMzUyN2VjNzU3MjI5MTAwNWVlMGVhNWQmbHNuPTIyNjA0MzI2OCZvYWlkPTZhNDA0MjMwMzkyMGIwNWM1YTQyMmU5MzMzNzExZTRhMWFkODhmZGFlMzUyN2VjNzU3MjI5MTAwNWVlMGVhNWQmcGxhdGZvcm09YW5kcm9pZCZwcmppZD0zOTc3OTAwNCZ0aW1lc3RhbXA9MTY5NTY5NzEzMTE5MyZzaWduPWFlMGQyOGM5OGJiZjgwOGY4ZGQwNzhlNmFmZTg4NDEyJmlzRGVidWc9MQ=="
decoded_url = requests.utils.unquote(url)
print(decoded_url)