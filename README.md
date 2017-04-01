# iosnewmonkey
new monkey tool for ios

1.You need to start WebDriverAgent by yourself

Follow the instructions in https://github.com/facebook/WebDriverAgent

2. After it is finished you can simply open WebDriverAgent.xcodeproj and start WebDriverAgentRunner test

It is better to start with Xcode to prevent CodeSign issues.

xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'platform=iOS Simulator,name=iPhone 6' test
Install python wda client

3. install wda by NetEase

pip install --pre facebook-wda

4. install usbmuxd
```
$ brew install usbmuxd
```

4. start proxy
```
iproxy 8100 8100
```

5. run scripts 
```
python testios.py bundleID actionNum
```
example: python testios.py com.pingan.EBankHuarui 100

