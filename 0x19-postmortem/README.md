Postmortem Report: Service Outage on May 20, 2024

Issue Summary: The Great API Timeout Debacle
Duration of Outage: May 20, 2024, 14:00 - 14:45 GMT
Impact: Our API service decided to take a nap, leaving about 40% of our users high and dry. Imagine a crowded restaurant where the chef goes on break—hungry patrons were left staring at empty plates (or in this case, timeout errors).

Timeline of Events: A Comedy of Errors
14:00 GMT - Alert! Monitoring systems buzzed like an over-caffeinated office worker. Error rates spiked, and our API service was MIA.
14:05 GMT - Engineers, with their super-sleuth hats on, began investigating. They found the service unresponsive and memory usage climbing faster than a cat up a tree.
14:15 GMT - We(i was barely watching on the sidelines) suspected a memory leak in our session handling (a sneaky culprit!) and dove into the application code.
14:25 GMT - Took a detour down the wrong alley—investigating database connectivity and network latency. Turns out, the database and network were not the villains here.
14:30 GMT - Escalation! The backend engineering team, our knights in shining armor, took over the investigation.
14:40 GMT - !!!! Discovered the real culprit: a memory leak in our session management. The issue was like a bad joke—painfully obvious in hindsight.
14:45 GMT - The issue was resolved. We applied a fix to the code, restarted the service, and our API woke up refreshed and ready to serve.

Root Cause and Resolution: The Mystery Unveiled
Cause: The memory leak was caused by our session management code holding onto memory like it was a prized possession. Sessions weren’t being released properly, leading to an ever-growing memory footprint.
Resolution: We gave the session management code a makeover, fixing the memory leak and deploying the updated code. A quick restart of the API service and everything was back to normal—like magic!

Corrective and Preventative Measures: How to Avoid the Next Comedy Show
Improvements/Fixes:
Memory Management Makeover: Review and optimize memory handling in all services to avoid future bloopers.
Stress Testing Overhaul: Add stress tests to the CI/CD pipeline to catch memory leaks before they catch us.
Monitoring Upgrades: Set up extra monitoring for memory usage—because we’d rather be safe than sorry.
Tasks:
Patch Application Code: Refactor the session management logic to avoid memory leaks.
Update Testing Protocols: Incorporate stress tests to simulate high load and detect memory issues.
Enhance Monitoring: Configure alerts for abnormal memory usage and service performance.
Post-Incident Debrief: Organize a review with the backend team to ensure everyone’s on the same page for future incidents.
