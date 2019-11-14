Step 1：

```
CUDA_REPO_PKG=cuda-repo-ubuntu1604_9.1.85-1_amd64.deb

wget -O /tmp/${CUDA_REPO_PKG} http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/${CUDA_REPO_PKG} 

sudo dpkg -i /tmp/${CUDA_REPO_PKG}

sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub 

rm -f /tmp/${CUDA_REPO_PKG}

sudo apt-get update

sudo apt-get install cuda-drivers
```

Step 2：

```
sudo apt-get install cuda
sudo apt-get install cuda-9-0
```

Step 3：

参考安装手册：https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html

```
sudo dpkg -i libcudnn7_7.3.1.20-1+cuda9.0_amd64.deb
```

Step 4：

https://docs.nvidia.com/deeplearning/sdk/nccl-install-guide/index.html

```
sudo dpkg -i nccl-repo-<version>.deb
```
