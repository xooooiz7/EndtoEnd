# End-to-end-Youtube-Sentiment

<!-- '''
🧠 Conda = ครบวงจร (สร้าง env + จัดการ dependencies + Python version ได้เลย)
🐍 venv = เบาและเรียบง่าย (แค่แยก env เฉย ๆ)

| ถ้า…                            | พี่แนะนำให้ใช้           |
| ------------------------------- | ------------------------ |
| ทำโปรเจกต์ AI / ML / MLOps      | 🟢 **Conda**             |
| แค่รัน script Python ทั่วไป     | 🟠 **venv**              |
| ต้องการสลับ Python หลายเวอร์ชัน | ✅ **Conda ง่ายกว่าเยอะ** |
| อยากได้ environment เบาและเร็ว  | ⚡ **venv ดีกว่า**        |

''' -->
# Create env by using conda
conda create -n youtube python=3.11 -y 

conda activate youtube

pip install -r requirements.txt


## DVC
<!-- | เป้าหมาย                           | ใช้ Git ได้ไหม  | ใช้ DVC แล้วดีกว่าไหม |
| ---------------------------------- | --------------- | --------------------- |
| เก็บโค้ดเท่านั้น                   | ✅ ได้เลย        | ❌ ไม่จำเป็น           |
| เก็บ dataset / model ด้วย          | ⚠️ ได้แต่ช้ามาก | ✅ DVC เหมาะสุด        |
| ทำ pipeline ML เต็มระบบ            | ❌ ไม่ได้        | ✅ ต้องใช้ DVC         |
| แชร์โปรเจกต์กับทีมแบบ reproducible | ❌ ยาก           | ✅ ง่ายมาก             |
 -->
dvc init

dvc repro

dvc dag


## AWS

aws configure



### Json data demo in postman

http://localhost:5000/predict

```python
{
    "comments": ["This video is awsome! I loved a lot", "Very bad explanation. poor video"]
}
```



chrome://extensions


## how to get youtube api key from gcp:

https://www.youtube.com/watch?v=i_FdiQMwKiw



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 016839106425.dkr.ecr.ap-southeast-2.amazonaws.com/mlproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
