import rclone
import os
import logging

project_name = os.environ['INPUT_PROJECT']
url_sp = os.environ['INPUT_URL_SP']
user = os.environ['INPUT_USER']
password = os.environ['INPUT_PASS']
auth_url = os.environ['INPUT_AUTH_URL']
token_url = os.environ['INPUT_TOKEN_URL']
client_id = os.environ['INPUT_CLIENT_ID']
client_secret = os.environ['INPUT_CLIENT_SECRET']
source_folder = os.environ['INPUT_SRC_FOLDER']
destination_folder = os.environ['INPUT_DST_FOLDER']

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s"
)

def build_cfg():
    obc_rclone = rclone.with_config("").run_cmd(command="obscure", extra_args=[password])
    obc_pass = obc_rclone.get('out').decode("utf-8")

    return """
    [sharepoint]
    type = sharepoint
    url = {0}
    vendor = sharepoint
    auth_url = {1}
    token_url = {2}
    client_id = {3}
    client_secret = {4}
    """.format(url_sp, auth_url, token_url, client_id, client_secret)

def main():
    cfg = build_cfg()
    result = rclone.with_config(cfg).run_cmd(command="copy", extra_args=[
        "--ignore-times",
        "--verbose",
        "/github/workspace/"+source_folder,
        "sharepoint:"+destination_folder
    ])

    print(result.get('out').decode("utf-8"))

main()