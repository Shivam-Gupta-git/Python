# Implement and exponential backoff strategy that double the wait time between retries, strings from 1 second, but stop after 5 retries.

import time

waitTime = 1
maxRetries = 5
attempts = 0

while attempts < maxRetries :
  print("Attempts", attempts + 1, "- Wait time",waitTime)
  time.sleep(waitTime)
  waitTime *= 2
  attempts += 1