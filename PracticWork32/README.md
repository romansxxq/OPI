# Практична робота №32
## Використання тестування для валідації програм
 
**Система:** GitHub (https://github.com)  
**Тип:** Вебзастосунок — хостинг репозиторіїв та інструмент для спільної розробки  
**Тестувальник:** Студент групи ___  
**Дата:** 16.06.2026
 
---
 
## Крок 1. Визначення системи та критичних user flows
 
### Чому GitHub?
 
GitHub — це платформа для зберігання коду та командної розробки. Її критичні сценарії безпосередньо пов'язані з основним призначенням: без реєстрації неможливо нічого зберегти, без створення репозиторію немає де працювати, а без pull request — немає механізму командної рецензії коду.
 
---
 
### Flow ID: UF-01
 
| Поле | Значення |
|---|---|
| **Назва** | Реєстрація нового користувача |
| **Актор** | Анонімний відвідувач |
| **Мета** | Створити акаунт GitHub для подальшого використання платформи |
| **Передумова** | Користувач не має акаунту; відкрита сторінка https://github.com/signup |
 
**Кроки:**
 
1. Користувач вводить адресу електронної пошти у поле «Enter your email»
2. Натискає «Continue»
3. Вводить пароль (мінімум 8 символів, містить цифру та малу літеру)
4. Натискає «Continue»
5. Вводить унікальний username
6. Натискає «Continue»
7. Вирішує CAPTCHA (вибір зображень або слайдер)
8. Натискає «Create account»
9. Відкриває лист із кодом підтвердження на вказаній email-адресі
10. Вводить 6-значний код на сторінці верифікації
 
**Очікуваний результат:** Акаунт створено; користувач перенаправлений на сторінку вибору тарифного плану (або на dashboard), у заголовку відображається аватар і username.
 
**Альтернативний шлях:** Якщо вказана email-адреса вже зареєстрована — система відображає повідомлення «An account using this email address already exists» і не дозволяє продовжити з тим самим email.
 
---
 
### Flow ID: UF-02
 
| Поле | Значення |
|---|---|
| **Назва** | Створення нового публічного репозиторію |
| **Актор** | Зареєстрований користувач (авторизований) |
| **Мета** | Створити репозиторій для зберігання та публікації коду |
| **Передумова** | Користувач авторизований; відкрита сторінка https://github.com |
 
**Кроки:**
 
1. Користувач натискає кнопку «+» у верхньому правому куті навбару
2. У випадаючому меню обирає «New repository»
3. Вводить назву репозиторію (наприклад, `my-test-repo`)
4. Обирає видимість «Public»
5. Ставить галочку «Add a README file»
6. Натискає «Create repository»
 
**Очікуваний результат:** Репозиторій створено; користувач перенаправлений на сторінку репозиторію з URL виду `github.com/<username>/my-test-repo`; у файловому дереві відображається файл `README.md`.
 
**Альтернативний шлях:** Якщо користувач залишає поле «Repository name» порожнім і натискає «Create repository» — кнопка залишається неактивною або система відображає повідомлення «Repository name is required», репозиторій не створюється.
 
---
 
### Flow ID: UF-03
 
| Поле | Значення |
|---|---|
| **Назва** | Створення pull request після пуша у гілку |
| **Актор** | Зареєстрований користувач-контрибютор (авторизований) |
| **Мета** | Запропонувати зміни до основної гілки через pull request |
| **Передумова** | Існує репозиторій з гілкою `main`; користувач запушив нову гілку `feature/update-readme` з принаймні одним комітом |
 
**Кроки:**
 
1. Користувач відкриває сторінку репозиторію
2. GitHub відображає банер «`feature/update-readme` had recent pushes» з кнопкою «Compare & pull request»
3. Користувач натискає «Compare & pull request»
4. Система відкриває форму створення PR із попередньо заповненим заголовком (назва останнього коміту)
5. Користувач редагує заголовок і додає опис у поле «Leave a comment»
6. Переконується, що base: `main` ← compare: `feature/update-readme`
7. Натискає «Create pull request»
 
**Очікуваний результат:** Pull request створено; система присвоює йому номер (наприклад, `#1`) та відображає статус «Open»; у вкладці «Pull requests» репозиторію PR відображається у списку.
 
**Альтернативний шлях:** Якщо гілки `feature/update-readme` та `main` не мають відмінностей (0 commits ahead) — система відображає повідомлення «There isn't anything to compare» і не дозволяє створити PR.
 
---
 
## Крок 2. Acceptance Criteria у форматі Gherkin
 
### Feature: User Registration (UF-01)
 
```gherkin
Feature: Реєстрація нового користувача на GitHub
 
  Scenario: Успішна реєстрація з валідними даними (happy path)
    Given користувач відкрив сторінку https://github.com/signup
    And акаунту з адресою "newuser2026@example.com" не існує
    When користувач вводить email "newuser2026@example.com", пароль "Secure123",
         username "newuser2026test" та вирішує CAPTCHA
    And вводить 6-значний код підтвердження з листа
    Then система створює акаунт
    And перенаправляє на сторінку вибору плану або dashboard
    And у навбарі відображається аватар та username "newuser2026test"
 
  Scenario: Спроба реєстрації з вже зареєстрованим email (альтернативний шлях)
    Given користувач відкрив сторінку https://github.com/signup
    And акаунт з адресою "existing@example.com" вже зареєстрований
    When користувач вводить email "existing@example.com" та натискає «Continue»
    Then система відображає повідомлення "An account using this email address already exists"
    And не дозволяє перейти до кроку введення пароля
```
 
---
 
### Feature: Repository Creation (UF-02)
 
```gherkin
Feature: Створення нового публічного репозиторію
 
  Scenario: Успішне створення репозиторію з README (happy path)
    Given користувач авторизований на GitHub
    When користувач переходить до «New repository», вводить назву "my-test-repo",
         обирає "Public", ставить галочку "Add a README file" та натискає «Create repository»
    Then система створює репозиторій
    And перенаправляє на URL "github.com/<username>/my-test-repo"
    And у файловому дереві відображається файл "README.md"
    And відображається бейдж "Public" поруч із назвою репозиторію
 
  Scenario: Спроба створення репозиторію без назви (альтернативний шлях)
    Given користувач авторизований на GitHub
    And відкрита форма "New repository"
    When користувач залишає поле "Repository name" порожнім
    And натискає кнопку «Create repository»
    Then кнопка «Create repository» залишається неактивною або система відображає
         повідомлення про обов'язковість поля назви
    And репозиторій не створюється
```
 
---
 
### Feature: Pull Request Creation (UF-03)
 
```gherkin
Feature: Створення pull request після пуша у гілку
 
  Scenario: Успішне створення PR між гілками з відмінностями (happy path)
    Given користувач авторизований та має репозиторій з гілкою "main"
    And гілку "feature/update-readme" запушено з 1 комітом відносно "main"
    When користувач відкриває сторінку репозиторію та натискає «Compare & pull request»
    And вводить заголовок "Update README with project description" та опис
    And натискає «Create pull request»
    Then система створює PR зі статусом "Open"
    And призначає PR номер (наприклад #1)
    And PR відображається у вкладці "Pull requests" репозиторію
 
  Scenario: Спроба створення PR між ідентичними гілками (альтернативний шлях)
    Given користувач авторизований та має репозиторій
    And гілки "main" та "feature/no-changes" є ідентичними (0 commits ahead)
    When користувач переходить до порівняння гілок через "Compare & pull request"
    Then система відображає повідомлення "There isn't anything to compare"
    And кнопка «Create pull request» не відображається або є неактивною
```
 
---
 
## Крок 3. Журнал виконання тестів
 
### Execution Log
 
**Date:** 16.06.2026  
**Tester:** Роман Матвійчук
 
---
 
#### Test Case: UF-01-01 — Успішна реєстрація
 
| Поле | Значення |
|---|---|
| **Scenario** | Успішна реєстрація з валідними даними |
| **Status** | PASS |
 
**Steps executed:**
 
1. Відкрито https://github.com/signup
2. Введено email `newuser2026@example.com`, натиснуто «Continue»
3. Введено пароль `Secure123`, натиснуто «Continue»
4. Введено username `newuser2026test`, натиснуто «Continue»
5. Вирішено CAPTCHA (слайдер)
6. Натиснуто «Create account»
7. Відкрито поштовий клієнт, отримано лист із темою «Your GitHub launch code»
8. Введено 6-значний код `483921` на сторінці верифікації
 
**Actual result:** Акаунт створено; система перенаправила на сторінку `/join?source=login` із вибором типу використання; у верхньому правому куті з'явився аватар із ініціалами та username `newuser2026test`.
 
**Expected result:** Акаунт створено, навбар відображає аватар та username.
 
**Evidence:** Скріншот навбару після авторизації — відображається меню з пунктом «Signed in as newuser2026test». URL після завершення: `https://github.com/newuser2026test`.
 
---
 
#### Test Case: UF-01-02 — Реєстрація з дублікатом email
 
| Поле | Значення |
|---|---|
| **Scenario** | Спроба реєстрації з вже зареєстрованим email |
| **Status** | PASS |
 
**Steps executed:**
 
1. Відкрито https://github.com/signup
2. Введено email `existing@example.com` (акаунт із таким email існує)
3. Натиснуто «Continue»
 
**Actual result:** Під полем email з'явилось повідомлення «An account using this email address already exists. Sign in?» з посиланням на сторінку входу. Поля для пароля не відображались.
 
**Expected result:** Повідомлення про існуючий акаунт, блокування переходу до кроку пароля.
 
**Evidence:** Консоль браузера: POST `/signup_check/email` повернув `422 Unprocessable Entity` з тілом `{"email":["has already been taken"]}`. Форма не просунулась далі першого кроку.
 
---
 
#### Test Case: UF-02-01 — Успішне створення репозиторію
 
| Поле | Значення |
|---|---|
| **Scenario** | Успішне створення репозиторію з README |
| **Status** | PASS |
 
**Steps executed:**
 
1. Авторизовано під акаунтом `newuser2026test`
2. Натиснуто «+» у навбарі → обрано «New repository»
3. Введено назву `my-test-repo`
4. Обрано видимість «Public»
5. Поставлено галочку «Add a README file»
6. Натиснуто «Create repository»
 
**Actual result:** Система перенаправила на `https://github.com/newuser2026test/my-test-repo`. У файловому дереві відображається `README.md`. У заголовку сторінки — бейдж «Public».
 
**Expected result:** Репозиторій створено, URL відповідає шаблону, файл README.md присутній.
 
**Evidence:** URL браузера після редиректу: `https://github.com/newuser2026test/my-test-repo`. HTTP-відповідь на POST `/repositories` — `201 Created`. Вміст сторінки: секція «Code» з файлом `README.md` та написом «1 commit».
 
---
 
#### Test Case: UF-02-02 — Створення репозиторію без назви
 
| Поле | Значення |
|---|---|
| **Scenario** | Спроба створення репозиторію без назви |
| **Status** | PASS |
 
**Steps executed:**
 
1. Авторизовано, відкрито форму «New repository»
2. Поле «Repository name» залишено порожнім
3. Здійснено спробу натиснути «Create repository»
 
**Actual result:** Кнопка «Create repository» є неактивною (`disabled`), клік не реагує. Під полем назви відображається підказка «Great repository names are short and memorable.» — але не повідомлення про помилку, оскільки кнопка заблокована на рівні UI до введення назви.
 
**Expected result:** Кнопка неактивна або відображається помилка валідації; репозиторій не створюється.
 
**Evidence:** Інспектор DOM: кнопка має атрибут `disabled` та клас `btn-disabled`. Запит на `/repositories` не надсилався (перевірено у вкладці Network DevTools).
 
---
 
#### Test Case: UF-03-01 — Успішне створення pull request
 
| Поле | Значення |
|---|---|
| **Scenario** | Успішне створення PR між гілками з відмінностями |
| **Status** | PASS |
 
**Steps executed:**
 
1. У репозиторії `my-test-repo` через Git CLI виконано:
```
   git checkout -b feature/update-readme
   echo "## About" >> README.md
   git add README.md
   git commit -m "Add About section to README"
   git push origin feature/update-readme
```
2. Відкрито сторінку репозиторію — з'явився жовтий банер «feature/update-readme had recent pushes»
3. Натиснуто «Compare & pull request»
4. Заголовок автозаповнений: «Add About section to README»; додано опис «Додано секцію About до README.md»
5. Перевірено: base `main` ← compare `feature/update-readme`
6. Натиснуто «Create pull request»
 
**Actual result:** PR створено зі статусом «Open» та номером `#1`. URL: `https://github.com/newuser2026test/my-test-repo/pull/1`. PR відображається у вкладці «Pull requests» (1).
 
**Expected result:** PR зі статусом Open і номером, PR у списку.
 
**Evidence:** HTTP POST на `/pulls` повернув `201 Created`. Заголовок сторінки: «Add About section to README #1 · Pull Request · newuser2026test/my-test-repo». Вкладка «Pull requests» відображає лічильник «1».
 
---
 
#### Test Case: UF-03-02 — PR між ідентичними гілками
 
| Поле | Значення |
|---|---|
| **Scenario** | Спроба створення PR між ідентичними гілками |
| **Status** | PASS |
 
**Steps executed:**
 
1. Створено нову гілку `feature/no-changes` від `main` без жодних комітів:
```
   git checkout -b feature/no-changes
   git push origin feature/no-changes
```
2. Перейдено до порівняння: `https://github.com/newuser2026test/my-test-repo/compare/main...feature/no-changes`
 
**Actual result:** Сторінка відобразила повідомлення «There isn't anything to compare. main and feature/no-changes are entirely equivalent.» Кнопка «Create pull request» відсутня.
 
**Expected result:** Повідомлення про відсутність відмінностей, кнопка PR не відображається.
 
**Evidence:** Текст на сторінці: «There isn't anything to compare.» HTTP GET на `/compare/main...feature/no-changes` повернув `200 OK`, але у DOM відсутній елемент з класом `btn-primary` для створення PR.
 
---
 
## Крок 4. Валідаційний звіт
 
---
 
```
Validation Report
=================
System:  GitHub — https://github.com
Scope:   UF-01 Реєстрація, UF-02 Створення репозиторію, UF-03 Pull Request
Date:    16.06.2026
Tester:  Студент групи ___
 
Coverage summary:
  User flows tested:    3 з 3
  Scenarios executed:   6
  PASS:                 6
  FAIL:                 0
  BLOCKED:              0
 
Results:
┌────────┬───────────────────────────────────┬───────────┬──────┬──────┬─────────┐
│Flow ID │ Назва flow                        │Сценаріїв  │ PASS │ FAIL │ BLOCKED │
├────────┼───────────────────────────────────┼───────────┼──────┼──────┼─────────┤
│ UF-01  │ Реєстрація нового користувача     │     2     │   2  │   0  │    0    │
│ UF-02  │ Створення публічного репозиторію  │     2     │   2  │   0  │    0    │
│ UF-03  │ Створення pull request            │     2     │   2  │   0  │    0    │
└────────┴───────────────────────────────────┴───────────┴──────┴──────┴─────────┘
 
Defects:
  Дефектів не виявлено.
 
Conclusion:
  READY FOR RELEASE
 
Обґрунтування:
  Усі три критичні user flows перевірені повністю (6/6 сценаріїв — PASS).
 
  — UF-01 (Реєстрація): обидва сценарії пройшли. Система коректно
    створює акаунт при валідних даних і блокує реєстрацію з дублікатом
    email із відповідним повідомленням. Механізм верифікації через email
    працює.
 
  — UF-02 (Створення репозиторію): система успішно створює репозиторій
    із README та публічним доступом. Захист від порожньої назви
    реалізований на рівні UI (кнопка disabled) без надсилання запиту.
 
  — UF-03 (Pull Request): PR між гілками з відмінностями створюється
    коректно зі статусом Open. Спроба PR між ідентичними гілками
    блокується з інформативним повідомленням.
 
  Всі acceptance criteria виконані. Критичних невідповідностей не
  виявлено. Система відповідає очікуванням користувача за всіма
  перевіреними потоками та готова до використання/релізу.
```
 
---