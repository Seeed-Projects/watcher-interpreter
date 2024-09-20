# Watcher Interpreter README

Welcome to the Watcher Interpreter, a command-line interface for interacting with your AI device. This tool allows you to configure your device, send commands, and interact with its functionalities.

## Setup

1. Install the Watcher package:

   ```bash
   pip install watcher-interpreter
   ```

2. Start the Watcher Interpreter:

   ```bash
   watcher-interpreter
   ```

   - tag: **setUser,setPwd,setEui FIRST!**

## Configuration Commands

Before using the device commands, you need to configure the necessary parameters.

- **setUser \<username\>**: Set the username (API key) for the device.

  ```sh
  > setUser 1ARRxxxMS250ZMZ2
  ```

- **setPwd \<password\>**: Set the password (API key) for the device.

  ```sh
  > setPwd 72Fxxxx6127A46FF89D95B8F7xxxxC1ACD54752706C344E1B02CD55Dxxxx2C1C
  ```

- **setEui \<eui\>**: Set the EUI of the device.

  ```sh
  > setEui 2xxxxx1C9627000xx
  ```

- **(optional)setBaseUrl \<url\>**: Set the base URL for the API.

  ```sh
  > setBaseUrl https://sensecap.seeed.cc/openapi/
  ```

## Device Commands

Once configured, you can use the following commands to interact with the device.

- **checkInfo**: Display the current configuration.

  ```sh
  > checkInfo
  ```

- **llm_chat \<words\>**: Send a chat message to the device.

  ```sh
  > llm_chat "Tell me a joke"
  Watcher:  {'data': {'tlid': 1726821849813, 'ctd': 1726821849813, 'tn': "Need a laugh? Here's a joke!", 'task_flow': [{'id': 6, 'type': 'chat', 'params': {'response': "Sure! Here's a classic one for you: Why don't skeletons fight each other? They don't have the guts! I hope that brought a smile to your face! Do you have a favorite joke you'd like to share?"}, 'wires': [[]]}]}, 'msg': '', 'code': '0'}
  ```

- **llm_task \<words\>**: Get a Task by message from the device.

  ```sh
  > llm_task Tell a joke when someone detected
  Task: <Task...JSON...too...long>
  ```

- **task_publish \<task\>**: Publish a task to the device.

  ```sh
  > llm_task Tell a joke when someone detected
  Task: <Task...JSON>
  > task_publish <Task...JSON>
  Watcher: {'code': '0', 'data': {}}
  ```

- **chat_publish \<words\>**: Send a message and publish it as a task.

  ```sh
  > chat_publish "Remind me about the meeting"
  # llm_task + task_publish
  Watcher: {'code': '0', 'data': {}}
  ```

- **chat \<words\>**: Chat with the device using a predefined task.

  ```sh
  > chat "What's the weather like today?"
  Watcher: The weather today is quite pleasant. ...
  ```

## Exiting the Program

- **exit**: Exit the Watcher Interpreter.

  ```sh
  > exit
  ```

## Additional Information

For developers, you can import the `watcher.sdk` module to interact with the device programmatically.

```python
import watcher.sdk

base_url = "https://sensecap.seeed.cc/openapi/"
# check https://sensecap-docs.seeed.cc/zh/httpapi_quickstart.html
user = "your api key ID"
pwd = "your api key secret"
# check your watcher 
eui = "your Watcher's EUI" 
result = watcher.sdk.llm_chat("why sky is blue?", base_url, user, pwd, eui)
print(result.get("data"))
```

## Support

For any issues or queries, please [New issue](https://github.com/Seeed-Projects/watcher-interpreter/issues)

## License

This software is licensed under the MIT License.
