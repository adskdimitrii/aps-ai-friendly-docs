# Generate Code Challenge

Source: https://aps.autodesk.com/en/docs/oauth/v2/tutorials/code-challenge/

---

# Generate Code Challenge

This walkthrough demonstrates how to generate code challenge for PKCE in OAuth 2.

## [Code Challenge](#code-challenge)

To authenticate public applications or single-page applications against Authorization server, it is recommended to adapt the Authorization Code flow with PKCE (Proof Key for Code Exchange). Here’s how it works.

- When the user initiates an authorization flow, the application computes a `code_verifier`. This is a random string between 43 and 128 characters and must contain only alphanumeric characters and punctuation characters `-`, `.`, `_`, `~`.
- Next up, the application computes a `code_challenge` starting from the `code_verifier`.

```
code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))

```

- The application directs the browser to a sign-in page along with the generated code challenge.
- Once the user authenticates, APS redirects back to your native application with an authorization code.
- Then, your application sends this code along with the code verifier to APS. APS returns an access token, refresh token, and optionally an ID token.

To generate the code challenge, we can employ the shell script.

### Using Shell Script

The following example illustrates the process.

Note that this script cannot be used to generate the actual code challenge but can be taken as a guideline.

```
code_verifier=$(openssl rand -base64 60 | tr -d "\n" | tr '/+' '_-' | tr -d '=')
echo "code_verifier=$code_verifier"
code_challenge=$(printf $code_verifier | shasum -a 256 | head -c 64 | xxd -r -p - | openssl base64 | tr '/+' '_-' | tr -d '=')
echo "code_challenge=$code_challenge"
echo "copied the code_challenge to your clipboard"
printf $code_challenge | pbcopy

```

## [Code Snippet for generating code_verifier and code_challenge for PKCE workflow](#code-snippet-for-generating-code-verifier-and-code-challenge-for-pkce-workflow)

### Python Version:

```
def vGenerateCodeChallengePair() -> tuple:
  code_verifier = base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8')
  code_verifier = re.sub('[^a-zA-Z0-9]+', '', code_verifier)

  code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
  code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8')
  code_challenge = code_challenge.replace('=', '')

  return (code_verifier, code_challenge)

```

Show More

### Java Version:

```
String generateCodeVerifier() throws UnsupportedEncodingException {
  SecureRandom secureRandom = new SecureRandom();
  byte[] codeVerifier = new byte[32];
  secureRandom.nextBytes(codeVerifier);
  return Base64.getUrlEncoder().withoutPadding().encodeToString(codeVerifier);
}

String generateCodeChallange(String codeVerifier) throws UnsupportedEncodingException, NoSuchAlgorithmException {
   byte[] bytes = codeVerifier.getBytes("US-ASCII");
   MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
   messageDigest.update(bytes, 0, bytes.length);
   byte[] digest = messageDigest.digest();
   return Base64.getUrlEncoder().withoutPadding().encodeToString(digest);
}

```

Show More

### C#.Net Core Version:

```
var pkce=new Pkce
{
  CodeVerifier = CryptoRandom.CreateUniqueId(32)
};
using (var sha256 = SHA256.Create())
{
  // Here we create a hash of the code verifier
  var challengeBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(pkce.CodeVerifier));

  // and produce the "Code Challenge" from it by base64Url encoding it.
  pkce.CodeChallenge = Base64Url.Encode(challengeBytes);
}

```

Show More

### Go Version:

```
import (
  "crypto/rand"
  _ "crypto/sha256"
  "encoding/base64"

  digest "github.com/opencontainers/go-digest"
)

const (
  size = 32
)

func GenerateCodeVerifier() string {
  b := make([]byte, size)
  if _, err := rand.Read(b); err != nil {
      return ""
  }
  return base64.URLEncoding.EncodeToString(b)
}

func GenerateCodeChallenge(codeVerifier string) string {
  byt := []byte(codeVerifier)
  digestAlg := digest.NewDigest(digest.SHA256, digest.SHA256.Hash())
  digestByte := digestAlg.Algorithm().FromBytes(byt)

  return base64.URLEncoding.EncodeToString([]byte(digestByte.String()))
}

```

Show More

### Javascript Version:

```
// Dependency: Node.js crypto module
// https://nodejs.org/api/crypto.html#crypto_crypto
function base64URLEncode(str) {
  return str.toString('base64')
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=/g, '');
}
var code_verifier = base64URLEncode(crypto.randomBytes(32));

// Dependency: Node.js crypto module
// https://nodejs.org/api/crypto.html#crypto_crypto
function sha256(buffer) {
  return crypto.createHash('sha256').update(buffer).digest();
}
var code_challenge = base64URLEncode(sha256(code_verifier));

```

Show More
