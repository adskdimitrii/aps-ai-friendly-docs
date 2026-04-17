# API Basics

Source: https://aps.autodesk.com/en/docs/ssa/developers_guide/api-basics/

---

# API Basics

## [What are Secure Service Accounts?](#what-are-secure-service-accounts)

Most applications accessing Autodesk Platform Services (APS) resources require users to sign in and grant permission to the applications. However, server-to-server applications operating in headless scenarios cannot prompt users for credentials or manual intervention. This is where Secure Service Accounts (SSAs) provide a solution, offering a secure authentication mechanism specifically designed for these headless scenarios to ensure seamless and secure access to resources.

## [How do SSAs work?](#how-do-ssas-work)

The Secure Service Account API lets you create up to 10 SSAs for each server-to-server application. Each SSA receives:

- A unique identifier
- A dedicated email address

Administrators use administrative consoles in various Autodesk services, including BIM 360, Forma, and Fusion Teams. Through these consoles, administrators can assign specific permissions to SSA email addresses. This permission assignment grants server-to-server applications the same access privileges as an actual user. The level of granularity depends on what the service’s permission model supports.

Assigning access privileges alone does not allow a headless application to access secured resources. The application needs to send a valid three-legged access token with each request to authenticate its identity.

To obtain an access token, server-to-server applications must first obtain a private key for the SSA. This requires calling the Create Keys </en/docs/ssa/v1/reference/http/ssa-create-service-account-key-POST/>_ operation. The private key displays only once and must be stored securely. This key is the foundation of the security model. Anyone possessing this key can potentially generate tokens with the same permissions as your SSA. We recommend using secure key management services appropriate for your hosting environment.

Once you obtain the private key, you must use it to generate a JSON Web Token (JWT) assertion. See [JWT Assertions](jwt-assertions.md) for more information. You can then use the [Exchange JWT Assertion for Token](../http-docs/http-ssa-exchange-jwt-assertion-POST.md) operation. This operation exchanges the JWT assertion for a three-legged access token. The token grants server-to-server applications permission to access the resources allowed for that SSA.

## [How are SSAs more secure?](#how-are-ssas-more-secure)

In the absence of SSAs, the industry has used a technique known as “User Impersonation”. SSAs are considered to be safer than user impersonation for several reasons:

- **Dedicated Authentication Mechanism:** SSAs use a dedicated authentication
mechanism. This mechanism is designed specifically for headless server-to-server
interactions. The method helps avoid risks associated with user credentials being
exposed or misused.
- **Granular Permissions:** SSAs allow administrators to assign specific
permissions to the SSA email addresses. This means the permissions can
be tailored precisely to what the server-to-server application needs,
minimizing the risk of over-privileged access, which is common in user
impersonation scenarios.
- **Token-Based Authentication:** SSAs use token-based authentication
rather than relying on user credentials. Tokens are typically
short-lived and can be easily revoked, reducing the risk associated
with long-term credential exposure.
- **Private Key Security:** The security model for SSAs relies on a
private key that is generated and stored securely. This key is the
foundation of the authentication process, and the use of secure key
management services helps protect it. In contrast, user impersonation
often involves storing and managing user passwords, which can be more
vulnerable to exposure and attacks.
- **Isolation of Service Accounts:** SSAs are isolated from regular user
accounts, meaning they are not tied to any individual’s credentials.
This reduces the risk of unauthorized access due to compromised user
accounts and ensures that service accounts can be managed
independently of user accounts.
- **Auditability and Monitoring:** Activities performed by SSAs can be
more easily monitored and audited compared to user impersonation.
Since SSAs are dedicated accounts, their actions can be tracked
separately, providing better visibility into server-to-server
interactions.
- **Compliance and Best Practices:** Using SSAs aligns with industry
best practices for secure authentication and compliance requirements.
It reduces the risk of violating policies related to user credential
management and ensures that server-to-server interactions adhere to
security standards.

## [Conclusion](#conclusion)

SSAs provide a robust and secure solution for server-to-server authentication, particularly in headless scenarios where user interaction is not possible. With the Secure Service Account API, you have all the tools required to manage SSAs and their associated private keys. This ensures secure access to resources for server-to-server applications, offering advantages such as enhanced security, granular permissions, token-based authentication, isolation of service accounts, and improved auditability.
