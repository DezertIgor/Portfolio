# Задача:

Исходя из информации на скриншоте ниже, составить логичные пары "Операционная система - Браузер" с помощью инструмента PICT.

![](./Задание%202.png)

Настройка сценариев в PICT:

```bash
Browser: Google Chrome, Firefox, Yandex Browser, Edge, Safari, Safari mobile, Chrome mobile
OS: Windows 10, Windows 8, Windows 7, MacOS, Android, iOS
if [OS]="iOS" then [Browser] like "*mobile";
if [Browser]="Safari mobile" then [OS]="iOS";
if [OS]="Android" then [Browser]="Chrome mobile";
if [Browser]="Chrome mobile" then [OS] in {"Android", "iOS"};
if [Browser]="Safari" then [OS]="MacOS";
```

Результат работы PICT:

| Browser        | OS         |
| -------------- | ---------- |
| Safari mobile  | iOS        |
| Firefox        | Windows 8  |
| Chrome mobile  | Android    |
| Edge           | Windows 8  |
| Firefox        | Windows 7  |
| Yandex Browser | Windows 7  |
| Edge           | Windows 7  |
| Google Chrome  | Windows 7  |
| Safari         | MacOS      |
| Chrome mobile  | iOS        |
| Edge           | Windows 10 |
| Yandex Browser | Windows 10 |
| Yandex Browser | MacOS      |
| Firefox        | Windows 10 |
| Edge           | MacOS      |
| Google Chrome  | Windows 8  |
| Yandex Browser | Windows 8  |
| Firefox        | MacOS      |
| Google Chrome  | MacOS      |
| Google Chrome  | Windows 10 |
