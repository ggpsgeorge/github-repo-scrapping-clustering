Feature: Search

Scenario: Search for term 'BDD' 
	Given a service running on https://www.google.com
	And a GET request to the resource /intl/en/about
	And the request has header 'Accept' with value '/*'
	When the response is received
	Then the response will have the status code 200
	And the response will have header 'Content-Type' with value 'text/html'
	And the response will not have a header 'foo' with value 'bar' 