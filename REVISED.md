# Gettop: Test Automation

## Description
In this test automation suite, built with Selenium and Pytest, key user interactions on the GetTop website are validated. It includes tests for navigating to the 'Tablets' page, checking the empty cart message, verifying the 'Login' page via the profile icon, and testing the search functionality with different keywords (e.g., 'chromebook' and 'samsung'). Each test ensures the correct page elements are displayed, with browser sessions set up and closed automatically before and after execution.

<img alt="Video Overview" src="https://i.imgur.com/FiW5j4j.mp4"/>
<img src="https://i.imgur.com/k636bYH.jpg" height="80%" width="80%" alt="Administrator Account"/>

## Concepts
- **Functional Testing**
- **Test Automation**
- **Basic ID and XPath locators**
- **Automation Scripts**

## Languages and Utilities Used
- **Selenium WebDriver**
- **Python**
- **PyCharm**
- **PyTest**
- **Chrome Dev Tools**

## Environments Used
- **Windows 11** (64bit)
- **macOS 12 Monterey**
- **Safari Version 5.1.7**
- **Chrome version 107.0.5304.87**

## Project Walk-through
Using Chrome Dev Tools to identify the XPath and locators through the HTML code of the website:

![XPath Identification](https://i.imgur.com/foIaaEm.png)

This Selenium script sets up a Chrome browser session and locates various elements on a web page, such as login fields, buttons, and navigation links, using different selectors like ID and XPath for potential interaction.

![Selenium Script](https://i.imgur.com/AomMswT.png)

Verifies that clicking the 'Tablets' link on the homepage opens the correct page.

![Tablets Link](https://i.imgur.com/WkkD2PP.png)

Confirms that an empty cart message is displayed after clicking the cart icon.

![Empty Cart Message](https://i.imgur.com/5VFFJhv.png)

Ensures clicking the user profile icon leads to the 'Login' page.

![Login Page](https://i.imgur.com/ZACzquy.png)

Tests the search functionality with various keywords (e.g., 'chromebook' and 'samsung') and verifies the correct search results page appears.

![Search Functionality](https://i.imgur.com/MQAssLf.png)