# KAIST-DataStructure-DynamicProgramming
문일철 교수님 데이터 구조 및 분석 : Linear Structure and Dynamic Programing 

## Installation 

- **git repository** 

```
git clone https://github.com/KIM-DKA/KAIST-DataStructure-DynamicProgramming.git
```

- **Direcrory** 

```
cd ocean_yard 
```
--- 
## Virtual Enviroment Setting

- Python version Download 

```
pyenv install python
```

- Check python3.10.12 PATH 
```
pyenv which python3.10
```

- virtual env install
```
pip install virtualenv 
```

- create virtual env
```
virtualenv kaist_env --python=<PYTHON_PATH>
``` 

- activate virtual env 

```
source kaist_env/bin/activate
```

- Project Packages Install 


```
pip install -r requirements.txt
```
 
---

## Python Environment

- **Language**: Python (3.10.12)
- **Database**: PostgreSQL (14.7)
- **Development Tools**: Visual Studio Code, Git, DBeaver, Drawio

## Development Standard

- **Code Style**: PEP 8, SQL Style Guide for Data Intelligence Team
- **Code Review**: GitHub Pull Requests
- **Git Convention**: Git Convention for Data Intelligence Team
- **Branched**: main(maintain), develop(maintain), feature(temporary), hotfix(temporary)
- **Merge Style**:
  - Push `feature` branch to the `develop` branch as `Rebase and Merge`
  - Push `hotfix` branch to the `develop` branch as `Rebase and Merge`
  - Push `develop` branch to the `main` branch as `Merge and Commit`
  
- **CI/CD**: GitHub Actions

--- 

## Git Branch Name Convention 

- **Feature Branches** 
    - 새로운 기능 개발을 위한 브랜치
    - feature/[issue번호]-[동사]-[기능명]
    - 예시: feature/1-add-dbconnector

2. Documents Branches 
    - 문서관련 파일 전부
    - docs/[issue번호]-[동사]-[기능명]
    - 예시: docs/2-add-readme-yaml

3. Hotfix Branches 
    - 디버깅 및 수정 
    - hotfix/[issue이슈번호]-[동사]-[버그명]
    - 예시: hotfix/3-fix-googleapi-key

## Commit Message Convention 

```
git commit -m '[Feat] Add DBHandler.py 
git commit -m '[Docs] Add README.md and config.yaml
```