# Id: OCST-1.2.1
# Status: Exploited
# Service: AWS S3
# STRIDE:
#   - Spoofing
# Components:
#   - Bucket versioning
# References:
#   - http://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html
#   - aws/s3/tools/s3bury


Feature: Hiding malicious data within object version history
  In order to avoid detection
  As an attacker
  I want to hide malicious files for later use


  Scenario: Burying files in S3 object history
    Given an S3 bucket with version history enabled
    And a principal with the ability to write to the bucket
    When the attacker uses the s3bury tool for their malicious files
    Then the latest version of the object still returns the original object
    And the attacker has a pre-signed and versioned url to download their malicious file
