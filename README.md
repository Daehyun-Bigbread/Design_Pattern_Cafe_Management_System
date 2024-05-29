# Design_Pattern_Cafe_Management_System
2024-1 Design Pattern Team Project Cafe Management System
# 카페 관리 시스템

## 내용 소개 및 목표
저희 프로젝트는 결제 관리 시스템, 재무제표, 카페 재고 관리 및 발주 관리 기능을 포함한 통합 카페 관리 시스템을 개발하는 것을 목표로 합니다.

## 세부 개발내용 진행 상황
각 팀원은 적어도 하나 이상의 패턴을 사용하여 결제 시스템, 재무제표, 카페 재고 관리 및 발주 시스템을 개발했습니다. 이를 통합하여 하나의 코드로 작성하고, 겹치는 부분을 해결하며 필요한 부분을 추가 개발했습니다.

## 기타 사항
- **참여 개발자:**

| 학과                        | 학번      | 이름      | 역할          |
|-----------------------------|-----------|-----------|---------------|
| 컴퓨터전자시스템공학부      | 202000449 | 김대현    | 팀장 / 개발    |
| 컴퓨터전자시스템공학부      | 202003766 | 홍승기    | 자료조사 / 개발 |
| 컴퓨터공학부                | 202200688 | 김성은    | 자료조사 / 개발 |

## 프로젝트 개발 타임라인

- **5/16 ~ 5/23:** 개인 담당 코드 작성
- **5/23 ~ 5/30:** 코드 통합 및 API 개발
- **5/30 ~ 6/04:** 발표 준비

## 개요

카페 관리 시스템은 카페 운영을 관리하기 위해 설계된 웹 기반 애플리케이션입니다. 사용자는 이 시스템을 통해 재고를 관리하고, 결제를 처리하며, 다양한 음료의 판매를 추적할 수 있습니다. 이 시스템은 Python을 사용한 Flask 백엔드 로직과 HTML, CSS, JavaScript로 구성된 프론트엔드 인터페이스를 통합합니다.

### 아키텍처

애플리케이션은 여러 주요 구성 요소로 구성되어 있습니다:

1. **백엔드 (Flask 서버)**:
    - 재고 관리, 결제 처리 및 음료 준비를 위한 API 엔드포인트를 관리합니다.
    - 재고 업데이트, 결제 처리 및 재무 추적을 위한 비즈니스 로직을 구현합니다.
    - HTTP 요청을 처리하기 위해 Flask를 사용하고, 크로스 오리진 요청 처리를 위해 Flask-CORS를 사용합니다.

2. **프론트엔드**:
    - 재고 관리, 결제 및 음료 준비를 위한 사용자 인터페이스를 제공합니다.
    - HTML, CSS 및 JavaScript로 구현되어 있으며, API 호출을 통해 백엔드와 통신합니다.

### 각 코드 모듈별 디자인 패턴 설명

#### 1. Payment Module

**사용한 디자인 패턴:**
- **전략 패턴 (Strategy Pattern)**: 결제 방식을 다르게 처리하기 위해 사용됨.


- **전략 패턴**: `PaymentStrategy` 인터페이스와 이를 구현한 `CardPayment`, `CashPayment`, `GiftPayment` 클래스들이 전략 패턴을 구성하여 다양한 결제 방식을 처리합니다.
- **팩토리 패턴**: `PaymentFactory` 클래스는 결제 방식에 따라 적절한 `PaymentStrategy` 객체를 생성합니다.

#### 2. Cafe Handler Module

**사용한 디자인 패턴:**
- **체인 오브 리스폰서빌리티 패턴 (Chain of Responsibility Pattern)**: 결제 요청을 처리하기 위해 사용됨.

- **체인 오브 리스폰서빌리티 패턴**: `CafeHandler` 클래스와 `Handler` 서브클래스 (`CashHandler`, `CreditCardHandler`, `DebitCardHandler`, `GifticonHandler`)는 결제 요청을 처리하기 위해 체인 오브 리스폰서빌리티 패턴을 사용합니다.

#### 3. Inventory Module

**사용한 디자인 패턴:**
- **싱글톤 패턴 (Singleton Pattern)**: 재고 관리 클래스가 단 하나의 인스턴스만 가지도록 보장하기 위해 사용됨.

- **싱글톤 패턴**: `InventoryManager` 클래스는 싱글톤 패턴을 사용하여 하나의 인스턴스만 존재하도록 보장합니다.

#### 4. Drink Module

**사용한 디자인 패턴:**
- **팩토리 패턴 (Factory Pattern)**: 음료 유형에 따라 적절한 음료 객체를 생성하기 위해 사용됨.


- **팩토리 패턴**: `DrinkFactory` 클래스는 음료 유형에 따라 적절한 `Drink` 객체를 생성합니다.

#### 5. Financial Module

**사용한 디자인 패턴:**
- **싱글톤 패턴 (Singleton Pattern)**: 재무 상태를 관리하는 클래스가 단 하나의 인스턴스만 가지도록 보장하기 위해 사용됨.
- **옵저버 패턴 (Observer Pattern)**:

 결제가 이루어질 때 재무 상태를 업데이트하기 위해 사용됨.

- **싱글톤 패턴**: `FinancialStatementSingleton` 클래스는 싱글톤 패턴을 사용하여 재무 상태를 관리합니다.
- **옵저버 패턴**: `Payment` 클래스는 `PaymentObserver` 인터페이스를 통해 관찰자를 추가하고 결제가 이루어질 때마다 관찰자에게 알림을 보냅니다. `FinancialStatementObserver` 클래스는 결제가 이루어질 때 재무 상태를 업데이트하는 옵저버입니다.

### 기술 스택

- **백엔드**: Python, Flask, Flask-CORS
- **프론트엔드**: HTML, CSS, JavaScript
- **디자인 패턴**: Singleton, Factory, Strategy, Observer, Chain of Responsibility
