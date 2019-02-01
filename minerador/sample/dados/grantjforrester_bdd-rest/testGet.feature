Feature: Test Get

Scenario: Get the resource representation 
	Given a service running on http://localhost:8080
	And a GET request to the resource /test-get
	And the request has a header 'inHeader' with value 'inValue'
	When the response is received
	Then the response will have the status code 200
	And the response will have a header 'outHeader' with value 'outValue'
	And the response will not have a header 'foo' with value 'bar' 
	And the response content will match 'someRepresentation'