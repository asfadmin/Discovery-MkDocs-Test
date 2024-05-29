let mkConsent = __md_get("__consent")
let asfConsentCookie = getCookie("consent");

if (asfConsentCookie !== "") {
  console.log("ASF consent cookie found: " + asfConsentCookie);
} else {
    console.log("ASF consent cookie not found");
}

if (mkConsent) {
  /* The user accepted the cookie */
    console.log("User accepted the cookie");
    setCookie("asfConsent", "accepted", 365);
} else {
  /* The user rejected the cookie */
    console.log("User rejected the cookie");
}
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/;domain=search.asf.alaska.edu";
}

function getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) === ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) === 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}