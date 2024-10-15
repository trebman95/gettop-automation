# Gettop: Test Automation

<h2>Description</h2>
In this project, I will walkthrough my API automation process using Postman to set up collections for organized API requests, using environment variables for flexibility, and writing test scripts to validate responses. I chain requests to simulate real-world workflows and conduct data-driven testing with external files to cover multiple test cases. I automated test execution by integrating Postman with CI/CD pipelines ensuring continuous testing and quality monitoring. In the Petstore API, JSON objects are used to interact with various aspects of the pet store. They represent data related to pets, orders, and users, allowing clients to create, update, retrieve, or delete these resources. 
<img src="https://i.imgur.com/k636bYH.jpg" height="80%" width="80%" alt="Administrator Account"/>
<br />

<h2>Concepts</h2>

- <b>Functional Testing</b>
- <b>Test Automation</b>
- <b>Basic ID and XPath locators</b>
- <b>Automation Scripts</b>


<h2>Languages and Utilities Used</h2>

- <b>Selenium WebDriver</b>
- <b>Python<b/>
- <b>PyCharm</b>
- <b>PyTest</b>

<h2>Environments Used </h2>

- <b>Windows 11</b> (64bit)</b>
- <b>macOS 12 Monterey</b>
- <b>Safari Version 5.1.7</b>
- <b>Chrome version 107.0.5304.87</b>

<h2>Project walk-through:</h2>

<p align="center">
This is the Swagger Editor that was used to access the pet store with JSON objects:  <br/>
<img src="https://i.imgur.com/vPP72Q6.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
A POST request is being made to the /pet endpoint at https://petstore.swagger.io/v2/pet. The request body contains a JSON object representing a new pet being added to the store : <br/>
<img src="https://i.imgur.com/foIaaEm.png" height="80%" width="80%" alt="Administrator Account"/>
<br />
<br />
A GET request is made to retrieve the details of a pet with the id 333997 from the Petstore API (/pet/{petId}). The response body shows the pet's details, such as id, name, category, tags, and status. :  <br/>
<img src="https://i.imgur.com/AomMswT.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
A PUT request is being made to update an existing pet's details in the Petstore API at the /pet endpoint. The pet with id 333997 is being updated, with the name changed to "Chico" and the photoUrls now containing two links. Added with scripts to check the response time less than 1 second. <br/>
<img src="https://i.imgur.com/WkkD2PP.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
A DELETE request is being made to detail an existing pet's details in the Petstore API at the /pet endpoint. The pet with id 333997 is identified as "unknown" with the status code of 200 OK :  <br/>
<img src="https://i.imgur.com/5VFFJhv.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
A GET request is being made to run the recent changes in the Petstore API. We see that there is a message of "Pet Not Found" after deleting a pet from the recent scripts.:  <br/>
<img src="https://i.imgur.com/ZACzquy.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Finally after running the results, the scripts have a 100% pass rate for automating the Petstore API :  <br/>
<img src="https://i.imgur.com/MQAssLf.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
</p>
