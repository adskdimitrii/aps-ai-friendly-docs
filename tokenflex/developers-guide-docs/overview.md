# Overview

Source: https://aps.autodesk.com/en/docs/tokenflex/developers_guide/overview/

---

# Overview

Autodesk Enterprise Token Flex is a licensing model that charges based on product usage. The Network License Reporting Service (NLRS), installed on each license server, sends consumption data to Autodesk, daily. There, the usage is tokenized and updated for Consumption Reporting (CORE).

The Token Flex Usage Data API allows enterprise customers using the Autodesk Token Flex/CORE platform to access their token consumption, product usage, and contract details. They can use this API to integrate CORE data with in-house reporting to facilitate charge-back automation. Contract Managers, Software Coordinators, Team Primary and Secondary Admins can use this API to generate reports at a level of detail (for example, session-wise, daily, monthly, annually) that makes most sense to them. What’s more, they can access both current and expired agreement usage data.

## [Common Use Cases](#common-use-cases)

- Query API: Generate customized reporting data. For example: Generate usage data for any desired custom date and for any subset of products or services. Create a snapshot containing desktop product usage by server by end user. Or create a view into desktop usage by product title and version. Merge any combination of data from current and expired contracts.
- Export API: Generate a customized CSV export file. For example: Combine Desktop with Cloud Products and Cloud Services data in a single file. Generate an export file for any date range, including spanning active and expired contracts.

## [Additional Use Cases](#additional-use-cases)

- Query a contract for agreement start and end dates.
- Query provisioned token pool amounts.
- Perform Export Report maintenance activities normally performed via Autodesk Account such as: create an export schedule, modify an existing schedule, delete a schedule, or delete an export file.
- Create and schedule multiple concurrent Export Report schedules.
