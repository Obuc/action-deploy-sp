import rclone
import os
import logging

project_name = os.environ['INPUT_PROJECT']
url_sp = os.environ['INPUT_URL_SP']
user = os.environ['INPUT_USER']
password = os.environ['INPUT_PASS']
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
    type = webdav
    url = {0}
    vendor = sharepoint
    user = {1}
    pass = {2}
    """.format(url_sp, user ,obc_pass)

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