2023-09-01 21:08:18 INFO ====== WebDriver manager ======
2023-09-01 21:08:20 INFO Get LATEST geckodriver version for 116.0 firefox
2023-09-01 21:08:20 DEBUG Starting new HTTPS connection (1): api.github.com:443
2023-09-01 21:08:20 DEBUG https://api.github.com:443 "GET /repos/mozilla/geckodriver/releases/latest HTTP/1.1" 200 2740
2023-09-01 21:08:20 INFO Get LATEST geckodriver version for 116.0 firefox
2023-09-01 21:08:20 DEBUG Starting new HTTPS connection (1): api.github.com:443
2023-09-01 21:08:21 DEBUG https://api.github.com:443 "GET /repos/mozilla/geckodriver/releases/latest HTTP/1.1" 200 2740
2023-09-01 21:08:21 INFO There is no [win64] geckodriver "v0.33.0" for browser firefox "116.0" in cache
2023-09-01 21:08:21 INFO Get LATEST geckodriver version for 116.0 firefox
2023-09-01 21:08:21 DEBUG Starting new HTTPS connection (1): api.github.com:443
2023-09-01 21:08:21 DEBUG https://api.github.com:443 "GET /repos/mozilla/geckodriver/releases/latest HTTP/1.1" 200 2740
2023-09-01 21:08:21 INFO Getting latest mozilla release info for v0.33.0
2023-09-01 21:08:21 DEBUG Starting new HTTPS connection (1): api.github.com:443
2023-09-01 21:08:21 DEBUG https://api.github.com:443 "GET /repos/mozilla/geckodriver/releases/tags/v0.33.0 HTTP/1.1" 200 2740
2023-09-01 21:08:21 INFO About to download new driver from https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip
2023-09-01 21:08:21 DEBUG Starting new HTTPS connection (1): github.com:443
2023-09-01 21:08:21 DEBUG https://github.com:443 "GET /mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip HTTP/1.1" 302 0
2023-09-01 21:08:21 DEBUG Starting new HTTPS connection (1): objects.githubusercontent.com:443
2023-09-01 21:08:22 DEBUG https://objects.githubusercontent.com:443 "GET /github-production-release-asset-2e65be/25354393/262910cf-b449-4db7-b4d9-e3de9b30d70a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230901T180731Z&X-Amz-Expires=300&X-Amz-Signature=df21b431dd36cca1434fd9288b0c0951cf4f551a3f5d635b0588020c27d3f4f3&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=25354393&response-content-disposition=attachment%3B%20filename%3Dgeckodriver-v0.33.0-win64.zip&response-content-type=application%2Foctet-stream HTTP/1.1" 200 1670449
2023-09-01 21:08:22 INFO Driver downloading response is 200
2023-09-01 21:08:22 INFO Get LATEST geckodriver version for 116.0 firefox
2023-09-01 21:08:22 DEBUG Starting new HTTPS connection (1): api.github.com:443
2023-09-01 21:08:23 DEBUG https://api.github.com:443 "GET /repos/mozilla/geckodriver/releases/latest HTTP/1.1" 200 2740
2023-09-01 21:08:23 INFO Driver has been saved in cache [C:\Users\Professional\.wdm\drivers\geckodriver\win64\v0.33.0]
2023-09-01 21:08:23 DEBUG Started executable: `C:\Users\Professional\.wdm\drivers\geckodriver\win64\v0.33.0\geckodriver.exe` in a child process with pid: 8620
2023-09-01 21:08:24 DEBUG POST http://localhost:58672/session {"capabilities": {"firstMatch": [{}], "alwaysMatch": {"browserName": "firefox", "acceptInsecureCerts": true, "moz:debuggerAddress": true, "pageLoadStrategy": "normal"}}}
2023-09-01 21:08:24 DEBUG Starting new HTTP connection (1): localhost:58672
2023-09-01 21:08:28 DEBUG http://localhost:58672 "POST /session HTTP/1.1" 200 0
2023-09-01 21:08:28 DEBUG Remote response: status=200 | data={"value":{"sessionId":"98078f7e-9174-4388-a833-1253111b0dd3","capabilities":{"acceptInsecureCerts":true,"browserName":"firefox","browserVersion":"116.0.2","moz:accessibilityChecks":false,"moz:buildID":"20230805021307","moz:debuggerAddress":"127.0.0.1:9222","moz:geckodriverVersion":"0.33.0","moz:headless":false,"moz:platformVersion":"10.0","moz:processID":8736,"moz:profile":"C:\\temp\\rust_mozprofileBj3tnC","moz:shutdownTimeout":60000,"moz:webdriverClick":true,"moz:windowless":false,"pageLoadStrategy":"normal","platformName":"windows","proxy":{},"setWindowRect":true,"strictFileInteractability":false,"timeouts":{"implicit":0,"pageLoad":300000,"script":30000},"unhandledPromptBehavior":"dismiss and notify"}}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '714', 'date': 'Fri, 01 Sep 2023 18:08:26 GMT'})
2023-09-01 21:08:28 DEBUG Finished Request
2023-09-01 21:08:28 INFO Test 1 is starting
2023-09-01 21:08:28 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/url {"url": "https://test-stand.gb.ru"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/url HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:28 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 INFO Send test to element Enter a login on an authorisation page
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"login\"]/div[1]/label/input"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"a85d554d-a024-446e-bfab-3ba533893568"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/a85d554d-a024-446e-bfab-3ba533893568/clear {"id": "a85d554d-a024-446e-bfab-3ba533893568"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/a85d554d-a024-446e-bfab-3ba533893568/clear HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/a85d554d-a024-446e-bfab-3ba533893568/value {"text": "test", "value": ["t", "e", "s", "t"], "id": "a85d554d-a024-446e-bfab-3ba533893568"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/a85d554d-a024-446e-bfab-3ba533893568/value HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 INFO Send test to element Enter a password on  an authorisation page
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"login\"]/div[2]/label/input"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"6cb2c914-c8d2-4dec-89be-3a73e6378d05"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/6cb2c914-c8d2-4dec-89be-3a73e6378d05/clear {"id": "6cb2c914-c8d2-4dec-89be-3a73e6378d05"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/6cb2c914-c8d2-4dec-89be-3a73e6378d05/clear HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/6cb2c914-c8d2-4dec-89be-3a73e6378d05/value {"text": "test", "value": ["t", "e", "s", "t"], "id": "6cb2c914-c8d2-4dec-89be-3a73e6378d05"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/6cb2c914-c8d2-4dec-89be-3a73e6378d05/value HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "css selector", "value": "button"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"0efaa489-e7dc-4568-bcd6-3ee99714b857"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/0efaa489-e7dc-4568-bcd6-3ee99714b857/click {"id": "0efaa489-e7dc-4568-bcd6-3ee99714b857"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/0efaa489-e7dc-4568-bcd6-3ee99714b857/click HTTP/1.1" 200 0
2023-09-01 21:08:30 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:30 DEBUG Clicked Login button
2023-09-01 21:08:30 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"app\"]/main/div/div/div[2]/h2"}
2023-09-01 21:08:30 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 404 0
2023-09-01 21:08:30 DEBUG Remote response: status=404 | data={"value":{"error":"no such element","message":"Unable to locate element: //*[@id=\"app\"]/main/div/div/div[2]/h2","stacktrace":"RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8\nWebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:187:5\nNoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:505:5\ndom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:132:16\n"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '423', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:30 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"app\"]/main/div/div/div[2]/h2"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 404 0
2023-09-01 21:08:31 DEBUG Remote response: status=404 | data={"value":{"error":"no such element","message":"Unable to locate element: //*[@id=\"app\"]/main/div/div/div[2]/h2","stacktrace":"RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8\nWebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:187:5\nNoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:505:5\ndom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:132:16\n"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '423', 'date': 'Fri, 01 Sep 2023 18:08:30 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"app\"]/main/div/div/div[2]/h2"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"937d25d1-dd74-408e-a36f-815458d4a67e"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG GET http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/937d25d1-dd74-408e-a36f-815458d4a67e/text {"id": "937d25d1-dd74-408e-a36f-815458d4a67e"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "GET /session/98078f7e-9174-4388-a833-1253111b0dd3/element/937d25d1-dd74-408e-a36f-815458d4a67e/text HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":"401"} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '15', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG Founded text 401 in field Get error text
2023-09-01 21:08:31 INFO Test 2 is starting
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/url {"url": "https://test-stand.gb.ru"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/url HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 INFO Send Stepan90 to element Enter a login on an authorisation page
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"login\"]/div[1]/label/input"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"9dcf9ed4-3bb0-4e66-9089-8eb577ba1c9e"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/9dcf9ed4-3bb0-4e66-9089-8eb577ba1c9e/clear {"id": "9dcf9ed4-3bb0-4e66-9089-8eb577ba1c9e"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/9dcf9ed4-3bb0-4e66-9089-8eb577ba1c9e/clear HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/9dcf9ed4-3bb0-4e66-9089-8eb577ba1c9e/value {"text": "Stepan90", "value": ["S", "t", "e", "p", "a", "n", "9", "0"], "id": "9dcf9ed4-3bb0-4e66-9089-8eb577ba1c9e"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/9dcf9ed4-3bb0-4e66-9089-8eb577ba1c9e/value HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 INFO Send feb966b76b to element Enter a password on  an authorisation page
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"login\"]/div[2]/label/input"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"c2359f1d-99de-4a4b-a91b-6518a30ef82d"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/c2359f1d-99de-4a4b-a91b-6518a30ef82d/clear {"id": "c2359f1d-99de-4a4b-a91b-6518a30ef82d"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/c2359f1d-99de-4a4b-a91b-6518a30ef82d/clear HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/c2359f1d-99de-4a4b-a91b-6518a30ef82d/value {"text": "feb966b76b", "value": ["f", "e", "b", "9", "6", "6", "b", "7", "6", "b"], "id": "c2359f1d-99de-4a4b-a91b-6518a30ef82d"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/c2359f1d-99de-4a4b-a91b-6518a30ef82d/value HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "css selector", "value": "button"}
2023-09-01 21:08:31 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:31 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"a72eb0a3-0d06-4570-b114-76e1ae624002"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:31 DEBUG Finished Request
2023-09-01 21:08:31 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/a72eb0a3-0d06-4570-b114-76e1ae624002/click {"id": "a72eb0a3-0d06-4570-b114-76e1ae624002"}
2023-09-01 21:08:32 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/a72eb0a3-0d06-4570-b114-76e1ae624002/click HTTP/1.1" 200 0
2023-09-01 21:08:32 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:32 DEBUG Finished Request
2023-09-01 21:08:32 DEBUG Clicked Login button
2023-09-01 21:08:32 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"app\"]/main/nav/ul/li[3]/a"}
2023-09-01 21:08:32 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 404 0
2023-09-01 21:08:32 DEBUG Remote response: status=404 | data={"value":{"error":"no such element","message":"Unable to locate element: //*[@id=\"app\"]/main/nav/ul/li[3]/a","stacktrace":"RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8\nWebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:187:5\nNoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:505:5\ndom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:132:16\n"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '420', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:32 DEBUG Finished Request
2023-09-01 21:08:32 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"app\"]/main/nav/ul/li[3]/a"}
2023-09-01 21:08:32 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 404 0
2023-09-01 21:08:32 DEBUG Remote response: status=404 | data={"value":{"error":"no such element","message":"Unable to locate element: //*[@id=\"app\"]/main/nav/ul/li[3]/a","stacktrace":"RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8\nWebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:187:5\nNoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:505:5\ndom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:132:16\n"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '420', 'date': 'Fri, 01 Sep 2023 18:08:31 GMT'})
2023-09-01 21:08:32 DEBUG Finished Request
2023-09-01 21:08:33 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"app\"]/main/nav/ul/li[3]/a"}
2023-09-01 21:08:33 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:33 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"2bbb3c23-3a9c-4a6a-806f-005b573d6597"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:33 GMT'})
2023-09-01 21:08:33 DEBUG Finished Request
2023-09-01 21:08:33 DEBUG GET http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/2bbb3c23-3a9c-4a6a-806f-005b573d6597/text {"id": "2bbb3c23-3a9c-4a6a-806f-005b573d6597"}
2023-09-01 21:08:33 DEBUG http://localhost:58672 "GET /session/98078f7e-9174-4388-a833-1253111b0dd3/element/2bbb3c23-3a9c-4a6a-806f-005b573d6597/text HTTP/1.1" 200 0
2023-09-01 21:08:33 DEBUG Remote response: status=200 | data={"value":"Hello, Stepan90"} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '27', 'date': 'Fri, 01 Sep 2023 18:08:33 GMT'})
2023-09-01 21:08:33 DEBUG Finished Request
2023-09-01 21:08:33 DEBUG Founded text Hello, Stepan90 in field Get login text
2023-09-01 21:08:33 INFO Test 3 is starting
2023-09-01 21:08:35 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "css selector", "value": "#create-btn"}
2023-09-01 21:08:35 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:35 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"484f3fee-69ec-4863-bc9f-be0f5098dae2"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:35 GMT'})
2023-09-01 21:08:35 DEBUG Finished Request
2023-09-01 21:08:35 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/484f3fee-69ec-4863-bc9f-be0f5098dae2/click {"id": "484f3fee-69ec-4863-bc9f-be0f5098dae2"}
2023-09-01 21:08:35 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/484f3fee-69ec-4863-bc9f-be0f5098dae2/click HTTP/1.1" 200 0
2023-09-01 21:08:35 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:35 GMT'})
2023-09-01 21:08:35 DEBUG Finished Request
2023-09-01 21:08:35 DEBUG Clicked Create post button
2023-09-01 21:08:37 INFO Send HW2 test to element Enter a title in a creating post form
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "/html/body/div/main/div/div/form/div/div/div[1]/div/label/input"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"bf48ef62-4284-4b61-8076-cfbe1c01c040"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/bf48ef62-4284-4b61-8076-cfbe1c01c040/clear {"id": "bf48ef62-4284-4b61-8076-cfbe1c01c040"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/bf48ef62-4284-4b61-8076-cfbe1c01c040/clear HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/bf48ef62-4284-4b61-8076-cfbe1c01c040/value {"text": "HW2 test", "value": ["H", "W", "2", " ", "t", "e", "s", "t"], "id": "bf48ef62-4284-4b61-8076-cfbe1c01c040"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/bf48ef62-4284-4b61-8076-cfbe1c01c040/value HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 INFO Send new description post to element Enter a description in a creating post form
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"11d20a99-e700-42bc-b531-88005255f15e"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/11d20a99-e700-42bc-b531-88005255f15e/clear {"id": "11d20a99-e700-42bc-b531-88005255f15e"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/11d20a99-e700-42bc-b531-88005255f15e/clear HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/11d20a99-e700-42bc-b531-88005255f15e/value {"text": "new description post", "value": ["n", "e", "w", " ", "d", "e", "s", "c", "r", "i", "p", "t", "i", "o", "n", " ", "p", "o", "s", "t"], "id": "11d20a99-e700-42bc-b531-88005255f15e"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/11d20a99-e700-42bc-b531-88005255f15e/value HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 INFO Send new content in the post to element Enter a content in a creating post form
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"2e8c2dfc-3e34-4b9e-8abb-e9c2957fc8ab"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/2e8c2dfc-3e34-4b9e-8abb-e9c2957fc8ab/clear {"id": "2e8c2dfc-3e34-4b9e-8abb-e9c2957fc8ab"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/2e8c2dfc-3e34-4b9e-8abb-e9c2957fc8ab/clear HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/2e8c2dfc-3e34-4b9e-8abb-e9c2957fc8ab/value {"text": "new content in the post", "value": ["n", "e", "w", " ", "c", "o", "n", "t", "e", "n", "t", " ", "i", "n", " ", "t", "h", "e", " ", "p", "o", "s", "t"], "id": "2e8c2dfc-3e34-4b9e-8abb-e9c2957fc8ab"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/2e8c2dfc-3e34-4b9e-8abb-e9c2957fc8ab/value HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "css selector", "value": ".mdc-button__label"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"72b45287-a63a-4166-acdb-29eb650d4ffc"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/72b45287-a63a-4166-acdb-29eb650d4ffc/click {"id": "72b45287-a63a-4166-acdb-29eb650d4ffc"}
2023-09-01 21:08:37 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/72b45287-a63a-4166-acdb-29eb650d4ffc/click HTTP/1.1" 200 0
2023-09-01 21:08:37 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:37 GMT'})
2023-09-01 21:08:37 DEBUG Finished Request
2023-09-01 21:08:37 DEBUG Clicked Save post button
2023-09-01 21:08:39 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"app\"]/main/div/div[1]/h1"}
2023-09-01 21:08:39 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:39 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"6cb39eca-87ac-4517-b965-1768a4e624d7"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:39 GMT'})
2023-09-01 21:08:39 DEBUG Finished Request
2023-09-01 21:08:39 DEBUG GET http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/6cb39eca-87ac-4517-b965-1768a4e624d7/text {"id": "6cb39eca-87ac-4517-b965-1768a4e624d7"}
2023-09-01 21:08:39 DEBUG http://localhost:58672 "GET /session/98078f7e-9174-4388-a833-1253111b0dd3/element/6cb39eca-87ac-4517-b965-1768a4e624d7/text HTTP/1.1" 200 0
2023-09-01 21:08:39 DEBUG Remote response: status=200 | data={"value":"HW2 test"} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '20', 'date': 'Fri, 01 Sep 2023 18:08:39 GMT'})
2023-09-01 21:08:39 DEBUG Finished Request
2023-09-01 21:08:39 DEBUG Founded text HW2 test in field Get post name
2023-09-01 21:08:39 INFO Test 4 is starting
2023-09-01 21:08:41 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "css selector", "value": "#app > main > nav > ul > li:nth-child(2) > a"}
2023-09-01 21:08:41 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:41 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"566ef4c9-d335-494f-a6f7-708dfd70774c"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:41 GMT'})
2023-09-01 21:08:41 DEBUG Finished Request
2023-09-01 21:08:41 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/566ef4c9-d335-494f-a6f7-708dfd70774c/click {"id": "566ef4c9-d335-494f-a6f7-708dfd70774c"}
2023-09-01 21:08:42 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/566ef4c9-d335-494f-a6f7-708dfd70774c/click HTTP/1.1" 200 0
2023-09-01 21:08:42 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:41 GMT'})
2023-09-01 21:08:42 DEBUG Finished Request
2023-09-01 21:08:42 DEBUG Clicked Contact Us button
2023-09-01 21:08:44 INFO Send Stepan Ivanov to element Enter an username in a contact us form
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"contact\"]/div[1]/label/input"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"1f0e8027-d246-4a3f-a6d4-b0cf3e72562c"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/1f0e8027-d246-4a3f-a6d4-b0cf3e72562c/clear {"id": "1f0e8027-d246-4a3f-a6d4-b0cf3e72562c"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/1f0e8027-d246-4a3f-a6d4-b0cf3e72562c/clear HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/1f0e8027-d246-4a3f-a6d4-b0cf3e72562c/value {"text": "Stepan Ivanov", "value": ["S", "t", "e", "p", "a", "n", " ", "I", "v", "a", "n", "o", "v"], "id": "1f0e8027-d246-4a3f-a6d4-b0cf3e72562c"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/1f0e8027-d246-4a3f-a6d4-b0cf3e72562c/value HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 INFO Send stepka@test.ru to element Enter an email in a contact us form
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"contact\"]/div[2]/label/input"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"cd86ee97-e227-40f0-a0d9-ffb092b0fee1"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/cd86ee97-e227-40f0-a0d9-ffb092b0fee1/clear {"id": "cd86ee97-e227-40f0-a0d9-ffb092b0fee1"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/cd86ee97-e227-40f0-a0d9-ffb092b0fee1/clear HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/cd86ee97-e227-40f0-a0d9-ffb092b0fee1/value {"text": "stepka@test.ru", "value": ["s", "t", "e", "p", "k", "a", "@", "t", "e", "s", "t", ".", "r", "u"], "id": "cd86ee97-e227-40f0-a0d9-ffb092b0fee1"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/cd86ee97-e227-40f0-a0d9-ffb092b0fee1/value HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 INFO Send Hi, guys! to element Enter a content in a contact us form
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "xpath", "value": "//*[@id=\"contact\"]/div[3]/label/span/textarea"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"1a101564-777a-4ba4-92f5-e69336d88575"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/1a101564-777a-4ba4-92f5-e69336d88575/clear {"id": "1a101564-777a-4ba4-92f5-e69336d88575"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/1a101564-777a-4ba4-92f5-e69336d88575/clear HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/1a101564-777a-4ba4-92f5-e69336d88575/value {"text": "Hi, guys!", "value": ["H", "i", ",", " ", "g", "u", "y", "s", "!"], "id": "1a101564-777a-4ba4-92f5-e69336d88575"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/1a101564-777a-4ba4-92f5-e69336d88575/value HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element {"using": "css selector", "value": "button"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":{"element-6066-11e4-a52e-4f735466cecf":"e1cf7f18-307c-4e86-a185-aebca9d7050d"}} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '88', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG POST http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/element/e1cf7f18-307c-4e86-a185-aebca9d7050d/click {"id": "e1cf7f18-307c-4e86-a185-aebca9d7050d"}
2023-09-01 21:08:44 DEBUG http://localhost:58672 "POST /session/98078f7e-9174-4388-a833-1253111b0dd3/element/e1cf7f18-307c-4e86-a185-aebca9d7050d/click HTTP/1.1" 200 0
2023-09-01 21:08:44 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:44 GMT'})
2023-09-01 21:08:44 DEBUG Finished Request
2023-09-01 21:08:44 DEBUG Clicked Save Contact Us form
2023-09-01 21:08:46 INFO Get alert text
2023-09-01 21:08:46 DEBUG GET http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/alert/text {}
2023-09-01 21:08:46 DEBUG http://localhost:58672 "GET /session/98078f7e-9174-4388-a833-1253111b0dd3/alert/text HTTP/1.1" 200 0
2023-09-01 21:08:46 DEBUG Remote response: status=200 | data={"value":"Form successfully submitted"} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '39', 'date': 'Fri, 01 Sep 2023 18:08:46 GMT'})
2023-09-01 21:08:46 DEBUG Finished Request
2023-09-01 21:08:46 DEBUG GET http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3/alert/text {}
2023-09-01 21:08:46 DEBUG http://localhost:58672 "GET /session/98078f7e-9174-4388-a833-1253111b0dd3/alert/text HTTP/1.1" 200 0
2023-09-01 21:08:46 DEBUG Remote response: status=200 | data={"value":"Form successfully submitted"} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '39', 'date': 'Fri, 01 Sep 2023 18:08:46 GMT'})
2023-09-01 21:08:46 DEBUG Finished Request
2023-09-01 21:08:46 INFO Form successfully submitted
2023-09-01 21:08:48 DEBUG DELETE http://localhost:58672/session/98078f7e-9174-4388-a833-1253111b0dd3 {}
2023-09-01 21:08:49 DEBUG http://localhost:58672 "DELETE /session/98078f7e-9174-4388-a833-1253111b0dd3 HTTP/1.1" 200 0
2023-09-01 21:08:49 DEBUG Remote response: status=200 | data={"value":null} | headers=HTTPHeaderDict({'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-cache', 'content-length': '14', 'date': 'Fri, 01 Sep 2023 18:08:48 GMT'})
2023-09-01 21:08:49 DEBUG Finished Request