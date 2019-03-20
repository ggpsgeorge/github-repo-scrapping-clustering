Feature: Test Post From File

Scenario: Post a new resource representation 
	Given a service running on http://localhost:8080
	And a POST request to the resource /test-post
	And the request has a header 'inHeader' with value 'inValue'
	And the request has content from file 'src/test/resources/com/github/grantjforrester/bdd/rest/resource.txt'
	When the response is received
	Then the response will have the status code 201
	And the response will have a header 'outHeader' with value 'outValue'
	And the response will not have a header 'foo' with value 'bar' 