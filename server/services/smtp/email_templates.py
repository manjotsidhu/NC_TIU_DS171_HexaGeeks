def load_signup_template():
    return '''\
    <!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Daftar</title>
    <style>
      body{{
        height:100% !important;
        margin:0;
        padding:0;
        width:100% !important;
      }}
      img{{
        border:0;
        outline:none;
        text-decoration:none;
      }}
      img{{
        width:auto;
        max-width:100%;
        display:block;
      }}
      a:hover{{
        color:#009999 !important;
      }}
      a:active{{
        color:#009999 !important;
      }}
      a:visited{{
        color:#009999 !important;
      }}
      .ReadMsgBody{{
        width:100%;
      }}
      .ExternalClass{{
        width:100%;
      }}
      img{{
        -ms-interpolation-mode:bicubic;
      }}
      body{{
        -ms-text-size-adjust:100%;
        -webkit-text-size-adjust:100%;
      }}
      body{{
        font-family:Arial,sans-serif;
        font-size:16px;
        font-weight:normal;
        line-height:24px;
        color:#4A4A4A;
      }}
      body{{
        background-color:#f4f4f4;
      }}
      .btn a:hover{{
        color:#fff !important;
      }}
      .btn a:active{{
        color:#fff !important;
      }}
      .btn a:visited{{
        color:#fff !important;
      }}
      @media only screen and (max-width: 600px){{
          body{{
              width:100% !important;
              min-width:100% !important;
              background-color: #ffffff !important;
          }}
      }}	@media only screen and (max-width: 600px){{
              body{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              table{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              td{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              p{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              a{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              li{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              blockquote{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              table{{
                  max-width:580px !important;
                  width:100% !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              #bodyTable{{
                  background-color: #ffffff !important;
              }}

      }} @media only screen and (max-width: 600px){{
              #bodyCell{{
                  padding:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-22{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-65{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-78{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-25{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-50{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-22:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-65:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-78:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-25:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-50:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .header-logo{{
                  padding:15px !important;
              }}

      }} @media only screen and (max-width: 600px){{
              .header{{
                  padding:20px !important;
                  border-radius:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .section{{
                  padding:20px !important;
                  border-radius:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .header{{
                  background:#3F3D55 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .product-block{{
                  background:#04158E !important;
              }}

      }} @media only screen and (max-width: 600px){{
              .footer .icon-text{{
                  display:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .is-fittogrid{{
                  width:100% !important;
                  height:auto !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .mobile-centered-container{{
                  text-align:center !important;
              }}

      }}	@media only screen and (max-width: 600px){{
        .mobile-centered-item{{
          display:inline-block !important;
        }}
      }}
  </style>
  </head>
  <body style="-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; background: #f4f4f4; color: #4A4A4A; font-family: Arial, sans-serif; font-size: 16px; font-weight: normal; height: 100% !important; line-height: 24px; margin: 0; padding: 0; width: 100% !important" bgcolor="#f4f4f4">
    <center>
      <table border="0" cellpadding="0" cellspacing="0" width="100%" id="bodyTable" style="height:100% !important;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#f4f4f4;border-collapse:collapse;color:#4A4A4A;font-family:Arial, sans-serif;font-size:16px;font-weight:normal;line-height:24px;margin:0;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:0;width:100% !important;" bgcolor="#f4f4f4">
        <tbody>
          <tr>
            <td align="center" valign="top" id="bodyCell" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;height:100% !important;margin:0;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:20px;width:100% !important;">
              <!-- // BEGIN EMAIL -->
              <table border="0" cellpadding="0" cellspacing="0" width="560" class="main" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                <tbody>
                  <!-- // OUTSIDE LOGO -->
                  <tr>
                    <td align="center" valign="top" class="header-logo" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:10px 50px 30px;">
                      <!-- // Logo block // -->
                      <a href="http://daftar-webapp.herokuapp.com" target="_blank" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#4DC3C9;text-decoration:none;"><img src="cid:DaftarLogo" alt="Daftar" width="146" height="30" style="-ms-interpolation-mode: bicubic; border: 0; display: block; max-width: 100%; outline: none; text-decoration: none; vertical-align: middle; width: auto"></a>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" valign="top" class="header" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background-color:#4caf50!important;background-size:560px 150px;border-radius:5px 5px 0 0;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:28px 130px;" bgcolor="#3F3D55">
                      <!-- // Header block // -->
                      <table border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                        <tbody>
                          <tr>
                            <td align="center" valign="middle" class="mobile-centered-container" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                              <h1 class="header-heading mobile-centered-item" style="color:#fff;font-size:24px;letter-spacing:-.43px;line-height:30px;margin:0;padding:0 0 20px;">Welcome to e-Daftar! Please verify your email</h1>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td align="left" valign="top" class="section is-top-merged" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#fff;border-radius:0 0 5px 5px;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:20px 50px 40px;" bgcolor="#ffffff">
                        <!-- Content section -->
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                          <tbody>
                            <tr>
                              <td align="left" valign="top" class="content-item" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;padding-bottom:25px;">
                                <h1 style="color:#4A4A4A;font-size:24px;letter-spacing:-.7px;line-height:29px;margin:0;padding:0;">
                                  <span class="highlighted-text" style="color: #000">Hi, {username}</span>
                                </h1>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" valign="top" class="content-item" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;padding-bottom:25px;">
                                <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;margin:0;">Thanks for signing up to E-Daftar, please verify your account to use the Paperless Office Portal.</p>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <table border="0" cellpadding="0" cellspacing="0" align="center" class="btn" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:separate;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                          <tbody>
                            <tr>
                              <td align="center" valign="middle" class="btn-content" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#FFE54C;border:2px solid #4a4a4a;border-radius:30px;color:#fff;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:4px 20px;" bgcolor="#A2F4DF">
                                <a href="http://daftar-webapp.herokuapp.com/verify={pin}" target="_blank" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#4a4a4a !important;display:block;font-family:Arial, sans-serif;font-size:13px;font-weight:bold;text-decoration:none;">Verify Account</a>
                              </td>
                            </tr>
                          </tbody>
                        </table>
						<table border="0" cellpadding="0" cellspacing="0" align="center" class="btn" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:separate;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                          <tbody>
                            <tr>
                              <td align="center" valign="middle" class="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:24px 20px;">
                                <small style="background:#ffffff;display:inline-block;letter-spacing:-.53px;margin:0;padding:10px 10px;">This is an automated generated mail from Daftar Server, please don't reply to it.</small>
							  </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                  </tbody>
                </table>
                <!-- END EMAIL // -->
              </td>
            </tr>
          </tbody>
        </table>
      </center>
    </body>
</html>
    '''


def load_notification_template():
    return '''\
    <!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Daftar</title>
    <style>
      body{{
        height:100% !important;
        margin:0;
        padding:0;
        width:100% !important;
      }}
      img{{
        border:0;
        outline:none;
        text-decoration:none;
      }}
      img{{
        width:auto;
        max-width:100%;
        display:block;
      }}
      a:hover{{
        color:#009999 !important;
      }}
      a:active{{
        color:#009999 !important;
      }}
      a:visited{{
        color:#009999 !important;
      }}
      .ReadMsgBody{{
        width:100%;
      }}
      .ExternalClass{{
        width:100%;
      }}
      img{{
        -ms-interpolation-mode:bicubic;
      }}
      body{{
        -ms-text-size-adjust:100%;
        -webkit-text-size-adjust:100%;
      }}
      body{{
        font-family:Arial,sans-serif;
        font-size:16px;
        font-weight:normal;
        line-height:24px;
        color:#4A4A4A;
      }}
      body{{
        background-color:#f4f4f4;
      }}
      .btn a:hover{{
        color:#fff !important;
      }}
      .btn a:active{{
        color:#fff !important;
      }}
      .btn a:visited{{
        color:#fff !important;
      }}
      @media only screen and (max-width: 600px){{
          body{{
              width:100% !important;
              min-width:100% !important;
              background-color: #ffffff !important;
          }}
      }}	@media only screen and (max-width: 600px){{
              body{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              table{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              td{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              p{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              a{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              li{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              blockquote{{
                  -webkit-text-size-adjust:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              table{{
                  max-width:580px !important;
                  width:100% !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              #bodyTable{{
                  background-color: #ffffff !important;
              }}

      }} @media only screen and (max-width: 600px){{
              #bodyCell{{
                  padding:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-22{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-65{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-78{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-25{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-50{{
                  display:block !important;
                  width:100% !important;
                  padding:0 0 15px !important;
                  box-sizing:border-box;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-22:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-65:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-78:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-25:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .column-50:last-child{{
                  padding-bottom:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .header-logo{{
                  padding:15px !important;
              }}

      }} @media only screen and (max-width: 600px){{
              .header{{
                  padding:20px !important;
                  border-radius:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .section{{
                  padding:20px !important;
                  border-radius:0 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .header{{
                  background:#3F3D55 !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .product-block{{
                  background:#04158E !important;
              }}

      }} @media only screen and (max-width: 600px){{
              .footer .icon-text{{
                  display:none !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .is-fittogrid{{
                  width:100% !important;
                  height:auto !important;
              }}

      }}	@media only screen and (max-width: 600px){{
              .mobile-centered-container{{
                  text-align:center !important;
              }}

      }}	@media only screen and (max-width: 600px){{
        .mobile-centered-item{{
          display:inline-block !important;
        }}
      }}
  </style>
  </head>
  <body style="-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; background: #f4f4f4; color: #4A4A4A; font-family: Arial, sans-serif; font-size: 16px; font-weight: normal; height: 100% !important; line-height: 24px; margin: 0; padding: 0; width: 100% !important" bgcolor="#f4f4f4">
    <center>
      <table border="0" cellpadding="0" cellspacing="0" width="100%" id="bodyTable" style="height:100% !important;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#f4f4f4;border-collapse:collapse;color:#4A4A4A;font-family:Arial, sans-serif;font-size:16px;font-weight:normal;line-height:24px;margin:0;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:0;width:100% !important;" bgcolor="#f4f4f4">
        <tbody>
          <tr>
            <td align="center" valign="top" id="bodyCell" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;height:100% !important;margin:0;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:20px;width:100% !important;">
              <!-- // BEGIN EMAIL -->
              <table border="0" cellpadding="0" cellspacing="0" width="560" class="main" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                <tbody>
                  <!-- // OUTSIDE LOGO -->
                  <tr>
                    <td align="center" valign="top" class="header-logo" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:10px 50px 30px;">
                      <!-- // Logo block // -->
                      <a href="http://daftar-webapp.herokuapp.com" target="_blank" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#4DC3C9;text-decoration:none;"><img src="cid:DaftarLogo" alt="Daftar" width="146" height="30" style="-ms-interpolation-mode: bicubic; border: 0; display: block; max-width: 100%; outline: none; text-decoration: none; vertical-align: middle; width: auto"></a>
                    </td>
                  </tr>
                  <tr>
                    <td align="left" valign="top" class="header" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background-color:#4caf50!important;background-size:560px 150px;border-radius:5px 5px 0 0;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:28px 130px;" bgcolor="#3F3D55">
                      <!-- // Header block // -->
                      <table border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                        <tbody>
                          <tr>
                            <td align="center" valign="middle" class="mobile-centered-container" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                              <h1 class="header-heading mobile-centered-item" style="color:#fff;font-size:24px;letter-spacing:-.43px;line-height:30px;margin:0;padding:0 0 20px;">You have a new notification!</h1>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td align="left" valign="top" class="section is-top-merged" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#fff;border-radius:0 0 5px 5px;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:20px 50px 40px;" bgcolor="#ffffff">
                        <!-- Content section -->
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                          <tbody>
                            <tr>
                              <td align="left" valign="top" class="content-item" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;padding-bottom:25px;">
                                <h1 style="color:#4A4A4A;font-size:24px;letter-spacing:-.7px;line-height:29px;margin:0;padding:0;">
                                  <span class="highlighted-text" style="color: #000">Hi, {username}</span>
                                </h1>
                              </td>
                            </tr>
                            <tr>
                              <td align="left" valign="top" class="content-item" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;padding-bottom:25px;">
                                <p style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;margin:0;">{content}</p>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <table border="0" cellpadding="0" cellspacing="0" align="center" class="btn" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:separate;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                          <tbody>
                            <tr>
                              <td align="center" valign="middle" class="btn-content" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;background:#FFE54C;border:2px solid #4a4a4a;border-radius:30px;color:#fff;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:4px 20px;" bgcolor="#A2F4DF">
                                <a href="http://daftar-webapp.herokuapp.com" target="_blank" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#4a4a4a !important;display:block;font-family:Arial, sans-serif;font-size:13px;font-weight:bold;text-decoration:none;">Open E-Daftar</a>
                              </td>
                            </tr>
                          </tbody>
                        </table>
						<table border="0" cellpadding="0" cellspacing="0" align="center" class="btn" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;border-collapse:separate;mso-table-lspace:0pt;mso-table-rspace:0pt;">
                          <tbody>
                            <tr>
                              <td align="center" valign="middle" class="" style="-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;mso-table-lspace:0pt;mso-table-rspace:0pt;padding:24px 20px;">
                                <small style="background:#ffffff;display:inline-block;letter-spacing:-.53px;margin:0;padding:10px 10px;">This is an automated generated mail from Daftar Server, please don't reply to it.</small>
							  </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                  </tbody>
                </table>
                <!-- END EMAIL // -->
              </td>
            </tr>
          </tbody>
        </table>
      </center>
    </body>
</html>
    '''