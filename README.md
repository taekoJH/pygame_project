Pygame RPG README 파일
개요
이 프로젝트는 Pygame을 사용하여 만든 간단한 2D RPG 게임입니다. 플레이어는 여러 레벨을 탐험하고 적과 싸우며 다양한 아이템을 수집할 수 있습니다.

요구 사항
이 게임을 실행하기 위해서는 다음이 필요합니다:

Python 3.8 이상
Pygame 2.0 이상
설치
Python이 설치되어 있는지 확인하세요. Python 다운로드

Pygame을 설치하세요:

sh
pip install pygame
프로젝트 폴더 안에 다음과 같은 파일 구조가 있는지 확인하세요:

css
pygame_project/
├── Images/
│   ├── Background.png
│   ├── Player_Sprite_R.png
│   ├── Player_Sprite_L.png
│   ├── Player_Sprite2_R.png
│   ├── Player_Sprite2_L.png
│   ├── Player_Sprite3_R.png
│   ├── Player_Sprite3_L.png
│   ├── Player_Sprite4_R.png
│   ├── Player_Sprite4_L.png
│   ├── Player_Sprite5_R.png
│   ├── Player_Sprite5_L.png
│   ├── Player_Sprite6_R.png
│   ├── Player_Sprite6_L.png
│   ├── Player_Attack1_R.png
│   ├── Player_Attack1_L.png
│   ├── Player_Attack2_R.png
│   ├── Player_Attack2_L.png
│   ├── Player_Attack3_R.png
│   ├── Player_Attack3_L.png
│   ├── Player_Attack4_R.png
│   ├── Player_Attack4_L.png
│   ├── Player_Attack5_R.png
│   ├── Player_Attack5_L.png
├── Game.py
├── Player.py
├── Ground.py
├── Enemy.py
├── RangedEnemy.py
├── UserInterface.py
├── LevelManager.py
├── HealthBar.py
├── Fireball.py
실행 방법
터미널을 열고 프로젝트 폴더로 이동하세요:

sh
cd path/to/pygame_project
게임을 실행하세요:

sh
python3 Game.py

게임 설명
조작법
왼쪽 방향키 (←): 왼쪽으로 이동
오른쪽 방향키 (→): 오른쪽으로 이동
스페이스바 (SPACE): 점프
엔터 (ENTER): 공격
숫자 키 (1, 2, 3, 4): 레벨 변경
H 키: 인벤토리 토글
M 키: 파이어볼 사용
P 키: 마나 포션 사용

게임 요소
플레이어: 기본적인 이동과 점프, 공격, 파이어볼 발사, 마나 포션 사용이 가능합니다.
적: 근접 적과 원거리 적이 있으며, 플레이어를 공격합니다.
아이템: 게임 내에서 다양한 아이템을 수집할 수 있습니다.
레벨: 다양한 레벨이 있으며, 각 레벨마다 다른 배경과 적이 등장합니다.
UI: 플레이어의 상태를 표시하는 사용자 인터페이스가 있습니다.

주요 클래스
Player: 플레이어 캐릭터를 관리합니다.
Enemy: 근접 적을 관리합니다.
RangedEnemy: 원거리 적을 관리합니다.
UserInterface: 사용자 인터페이스를 관리합니다.
LevelManager: 레벨을 관리합니다.
HealthBar: 플레이어의 체력바를 관리합니다.
Fireball: 플레이어가 발사하는 파이어볼을 관리합니다.
