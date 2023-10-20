import yaml
import os


DOCKER_REGISTRY = os.getenv("DOCKER_REGISTRY")
DOCKER_REPO = os.getenv("DOCKER_REPO")
SC = os.getenv("SC")
NAME_SPACE = os.getenv("NAME_SPACE")


# 修改job_init.yaml
with open("./yamls/l2-init/job_init.yaml", "r") as stream:
    try:
        yaml_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

yaml_data["spec"]["template"]["spec"]["initContainers"][0]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-deployer:compiled'
yaml_data["spec"]["template"]["spec"]["containers"][0]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-node'

with open("./yamls/l2-init/job_init.yaml", "w") as outfile:
    try:
        yaml.safe_dump(yaml_data, outfile, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)


# 修改sts_sequencer.yaml
with open("./yamls/l2-sequencer/sts_sequencer.yaml", "r") as stream:
    try:
        yaml_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

yaml_data["spec"]["template"]["spec"]["initContainers"][0]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-geth'
yaml_data["spec"]["template"]["spec"]["containers"][0]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-geth'
yaml_data["spec"]["template"]["spec"]["containers"][1]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-node'
yaml_data["spec"]["template"]["spec"]["containers"][2]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-batcher'
yaml_data["spec"]["volumeClaimTemplates"][0]["spec"]["storageClassName"] = SC

with open("./yamls/l2-sequencer/sts_sequencer.yaml", "w") as outfile:
    try:
        yaml.safe_dump(yaml_data, outfile, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)


# 修改sts_verifier.yaml
with open("./yamls/l2-verifier/sts_verifier.yaml", "r") as stream:
    try:
        yaml_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

yaml_data["spec"]["template"]["spec"]["initContainers"][0]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-geth'
yaml_data["spec"]["template"]["spec"]["containers"][0]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-geth'
yaml_data["spec"]["template"]["spec"]["containers"][1]["image"] = DOCKER_REGISTRY + '/' + DOCKER_REPO + '/op-node'
yaml_data["spec"]["volumeClaimTemplates"][0]["spec"]["storageClassName"] = SC

with open("./yamls/l2-verifier/sts_verifier.yaml", "w") as outfile:
    try:
        yaml.safe_dump(yaml_data, outfile, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)


# 修改pvc_config.yaml
with open("./yamls/l2-init/pvc_config.yaml", "r") as stream:
    try:
        yaml_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

yaml_data["spec"]["storageClassName"] = SC

with open("./yamls/l2-init/pvc_config.yaml", "w") as outfile:
    try:
        yaml.safe_dump(yaml_data, outfile, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)


# 修改sts_explorer.yaml
with open("./yamls/l2-explorer/sts_explorer.yaml", "r") as stream:
    try:
        yaml_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

yaml_data["spec"]["volumeClaimTemplates"][0]["spec"]["storageClassName"] = SC

with open("./yamls/l2-explorer/sts_explorer.yaml", "w") as outfile:
    try:
        yaml.safe_dump(yaml_data, outfile, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)
