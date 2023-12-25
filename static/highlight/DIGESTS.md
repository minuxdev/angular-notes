## Subresource Integrity

If you are loading Highlight.js via CDN you may wish to use [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) to guarantee that you are using a legimitate build of the library.

To do this you simply need to add the `integrity` attribute for each JavaScript file you download via CDN. These digests are used by the browser to confirm the files downloaded have not been modified.

```html
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
  integrity="sha384-xBsHBR6BS/LSlO3cOyY2D/4KkmaHjlNn3NnXUMFFc14HLZD7vwVgS3+6U/WkHAra"></script>
<!-- including any other grammars you might need to load -->
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/go.min.js"
  integrity="sha384-WmGkHEmwSI19EhTfO1nrSk3RziUQKRWg3vO0Ur3VYZjWvJRdRnX4/scQg+S2w1fI"></script>
```

The full list of digests for every file can be found below.

### Digests

```
sha384-SXyBDWbbsvVyOn5TICWCahSdE/E+YqByrDZhk5477SMEixaEUJr8NzFO9Qjyhsin /es/languages/asciidoc.js
sha384-t9QnTos94FrBBrAC7s5wV5c/I48x4nw+3vsiNa9XwkyyQih5RbUUSqt2Gd4uSfkG /es/languages/asciidoc.min.js
sha384-u/MnWLPAdhUSLvSy9g3lRTFAwZSiveQjbKCTRw58BJh5n/RQfyyiwweCohM8LeSM /es/languages/awk.js
sha384-UjBtWlHRGRibzEDg1rIFn+Q1OGqWCyMh3RkUN9+hDW27sIB2j8mcGvxmkk8l8LVM /es/languages/awk.min.js
sha384-uBlc/xEFeDxZmBU7K/YWwi3ryXQrLQCAY2K1Dl3OD2DaAQBZZTt6Ew3aeDP20ix0 /es/languages/bash.js
sha384-4qer4rJCVxZjkwD4YaJfOnT2NOOt0qdjKYJM2076C+djiJ4lgrP1LVsB/MCpJSET /es/languages/bash.min.js
sha384-DA5ii4oN8R2fsamNkHOanSjuN4v7j5RIuheQqnxMQ4cFnfekeuhwu4IdNXiCf+UU /es/languages/css.js
sha384-OBugjfIr093hFCxTRdVfKH8Oe3yiBrS58bhyYYTUQJVobk6SUEjD7pnV8BPwsr8a /es/languages/css.min.js
sha384-WFJdA9Hz+G9NQx5vPba/tcGyIibm57UkKVY32wNB/94iT2FmPma5W7gY8p2l6qps /es/languages/java.js
sha384-coaxfgI2lKuDqSxfMlfyPq5WM0THaLGyATZHzaFMrWdIbPcLdduuItTe6AmT/m33 /es/languages/java.min.js
sha384-WCznKe2n87QvV/L1MlXN+S8R6NPUQGU34+AqogMuWGZJswSD6rt3Mgih+xuKlDgm /es/languages/javascript.js
sha384-eGsBtetyKPDKaLiTnxTzhSzTFM6A/yjHBQIj4rAMVaLPKW5tJb8U6XLr/AikCPd+ /es/languages/javascript.min.js
sha384-12GbYFzdyZCSmfBTmO2CR/qE89K5uE1PEuJ3QUwXH0Q9u+uoLNigjH9dG7LAxxiI /es/languages/json.js
sha384-+DT7AtubDhVDciRc6CgjJJRsCt0L8NC3Dh8n9Tj2tZWU8rWxDIj1ViubmUDn8OCY /es/languages/json.min.js
sha384-OkDbf1Slbqz4CwuUJVZyhq9SKn5vYk5ADIxIBS3iV5D0ZY7T3g3BOGZgd9u0kyZH /es/languages/lua.js
sha384-wvrGnUzHwJzO9dWQFF2DxrFjkSPw5gmc0iOQYmJUzeZ4tqa+15VEFRCH4GI2DNF3 /es/languages/lua.min.js
sha384-bWwkdmOCj83zZ8/m+oPD9goRMhrPCb25ZA6aTyg7vcsq9IpuyED38kQSw1Na4UTZ /es/languages/markdown.js
sha384-SqGSUq0DMQ0OUQnQnTuVDCJyhANd/MFNj+0PF67S+VXgHpR8A4tPsf/3GoSFRmrx /es/languages/markdown.min.js
sha384-ohJ9Jj8Mwyy7EntP4tGMJEtH90WJNKu2C4l37N1kqyTHgbRJyGYUgFe9z3qy3/C8 /es/languages/nginx.js
sha384-tpFPEHvbpL3dYF4uFiVNuCUF62TgMzuW65u5mvxnaJYun1sZwxBsKv+EvVgv3yQK /es/languages/nginx.min.js
sha384-6eW/GwBjd1p/IWWvPhtlCq8ZV/viLec5e+CL+RdqEVMAfnyfcuqhDzNA/eADmRK0 /es/languages/pgsql.js
sha384-zOSNwldQX3ufsVxttzdDmDOl9B8zrMIbr7l0ixGfdle/Ree4OxUJK7kQjCDqT45z /es/languages/pgsql.min.js
sha384-PpU3S+yZJ1Gj2R7L/OgTgkKELQOf7F1VcbaAEJwSFSM9lw2ON2wxq1FvUcUlm9ne /es/languages/powershell.js
sha384-pBczxETXXX/Ne92jpBviT47DPiv27FLNtvs0aMZH3W7rYXdwgf1gWg3pH4NmNC2V /es/languages/powershell.min.js
sha384-+5oyk7Ed3OlvEWGj8xracq/6e52BScKUN4kxcreNwB7kfRTVsAMs/aAJM58dzIFN /es/languages/python.js
sha384-ND/UH2UkaeWiej5v/oJspfKDz9BGUaVpoDcz4cof0jaiv/mCigjvy7RQ7e+3S6bg /es/languages/python.min.js
sha384-lRhSX2XDrY27NzrAS1t4YaeRtwjsY41kFBbIEYltkmnsfSE7lbBJMQVds2u/MqTT /es/languages/scss.js
sha384-RDUehV4j9Do6iGkYq9Gjn3aUxh6x+NFER1sHpLUXsNoCFjah8Ysrlad8ukLbIr4J /es/languages/scss.min.js
sha384-rBAFhyrcRcMNbVJ9g4k5y3eQDkjGdgoOb3oTWTbHgwyUgUNv3CK9wLsGy/d+52oa /es/languages/sql.js
sha384-8G3qMPeOeXVKZ0wGzMQHgMVQWixLw3EXFAcU+IFNLRe0WoZB5St3L3ZLTK62Nzns /es/languages/sql.min.js
sha384-G1Opo3HxELoJ+Z/56DILHVhE3vs0B5gDypWNlWxjd4T6tE+KuV8dvFmDD4qKFAqQ /es/languages/stylus.js
sha384-xDDS9KwHtv72OFksAoRLSOzzD4H5DFtcSDwClXtktWSgfzUa5GBVC+QCa+JbXJo6 /es/languages/stylus.min.js
sha384-ckZPeKyE8cW29gT8AxdZNWMC96H8wZCpBzPVkyvuqsGIDvYIzEyxJcckwbv/afrk /es/languages/vim.js
sha384-8kEj1LOKOKcz1ifO10aWlws8zNCnrxWFhHS5zWENNU+dOB/z0X/X31StZHBTQ64Z /es/languages/vim.min.js
sha384-MX3xn8TktkjONV3aWF6Qn6WZyq2Lh/98p0v7D0qEoJ4WLdYjoAyXF/L/80q3qaEc /es/languages/yaml.js
sha384-4IiaMbQ0LBiRJYBGoAXsN+dV9qu/cGLES6IuVowdeCu/FAMY5/MQfD/bHXoL2YBb /es/languages/yaml.min.js
sha384-HPT+hE+CRAgt+UgsOWKsXyconKSjRIbAxiWxwmmQ3L3ijW6pi0tvaMpnT0vNORvu /languages/asciidoc.js
sha384-sf6kQzw438VELcTHWkS4YdEyIzCPQbGZLke4v5rtAIBrnGsuvCILPWGeIcDIVLmX /languages/asciidoc.min.js
sha384-xfaX9UdEVoIlYoDcsxk5OO1ddyQ0fl/BmWflf6SctNce+UzNDEimoWGmLbk0FTPg /languages/awk.js
sha384-+kQeWvlXeWctdKQQ8iGrG1JdmiKRJHAqofS2vKNnJ24H25HqMhb9kIQC3NYrsoch /languages/awk.min.js
sha384-qbbaBGYYg7PdopdWOGj8KdkBosUDY5PAe3aTMJKTqWcriPBJJzCVu5BlwNEwqr9U /languages/bash.js
sha384-ByZsYVIHcE8sB12cYY+NUpM80NAWHoBs5SL8VVocIvqVLdXf1hmXNSBn/H9leT4c /languages/bash.min.js
sha384-r9czyL17/ovexTOK33dRiTbHrtaMDzpUXW4iRpetdu1OhhckHXiFzpgZyni2t1PM /languages/css.js
sha384-HpHXnyEqHVbcY+nua3h7/ajfIrakWJxA3fmIZ9X9kbY45N6V+DPfMtfnLBeYEdCx /languages/css.min.js
sha384-pYIeBYeCE96U9EkPcT4uJjNWyrB1BKB41JIadYJbvmGa5KacaoXtSQOUpBfeyWQX /languages/java.js
sha384-uUg+ux8epe42611RSvEkMX2gvEkMdw+l6xG5Z/aQriABp38RLyF9MjDZtlTlMuQY /languages/java.min.js
sha384-vJxw3XlwaqOQr8IlRPVIBO6DMML5W978fR21/GRI5PAF7yYi2WstLYNG1lXk6j9u /languages/javascript.js
sha384-44q2s9jxk8W5N9gAB0yn7UYLi9E2oVw8eHyaTZLkDS3WuZM/AttkAiVj6JoZuGS4 /languages/javascript.min.js
sha384-dq9sY7BcOdU/6YaN+YmFuWFG8MY2WYJG2w3RlDRfaVvjdHchE07Ss7ILfcZ56nUM /languages/json.js
sha384-RbRhXcXx5VHUdUaC5R0oV+XBXA5GhkaVCUzK8xN19K3FmtWSHyGVgulK92XnhBsI /languages/json.min.js
sha384-/Ml+gzp/rkQcZkCwBqpVjCj028T6aTnOF/LCRJH8LBE5xcPcTkntQwJ5KGMMNLI3 /languages/lua.js
sha384-T04Yu4dcDCykCMf4EbZ62u3nURYEVkpphRGFhF/cMu+NrtDqoRHgbVOZz7hHdcaO /languages/lua.min.js
sha384-U+zIQPoVdPCO0o4poik2hYNbHtNm+L5OojDTulgIeEZTNz+LooLAm72d66mNjwKD /languages/markdown.js
sha384-mCUujHHbWJEjcupTTfWOk9YR3YCYNHaA578+TTXUd4LPi7fGNuMQbysbl1pmcIGd /languages/markdown.min.js
sha384-OtoDZeQykEsQoFzaA50vgmgr+D3F8WIaXZ0CZfYFivHEpkwCpRKT5Ptmuhjr5bfJ /languages/nginx.js
sha384-p6UV3HZc7zs9wUF6j4Knk3bpx1/JnhlwDoFnKJAOogB1cUi32u31NlnZ2s2dW8IR /languages/nginx.min.js
sha384-FbyEf9EotuzOvgY88yzeCiAnYTkV2uHiY+FkYU9uH1jJY/DmF8IvxDo0rnl4n3ug /languages/pgsql.js
sha384-Oo+KBAbqcXAtR0/yFlZsRvJSAITfvxhJ761p5yOO4pyEtYO6n/5j6eVI1dG8aGct /languages/pgsql.min.js
sha384-BW3J/7iREOC3EuqJwzGkDJb6FY9bVvkt70ipieV892fYAp8uReDMiO0/lrUPmkzL /languages/powershell.js
sha384-LWJZQx0dgGhEK7snfNYrQs5K+QKD1sOmE02sOQCz4br9UmqSJDvPLoUVFaUyFnjq /languages/powershell.min.js
sha384-zdZio5RcGiKQJCpe/1IXujPle3bIY8sbmvCabSU5G5GzWAzZtoRZfg9QAQXCL08q /languages/python.js
sha384-IP4vv4Aoh9Lyg8QyzVkAmn2JGoDCpgVHzVSrD3Z+rVyn7+s4wx4pRjv+go3TEwfj /languages/python.min.js
sha384-fwYddFsITuK2bPhi9RuIzwi4PTULEXgtEJsQzTdx97vOS/GHfrk+aNSLxEHgzQa5 /languages/scss.js
sha384-6u+QpCDqQidb5pcO+yBqy0xLJ30x30VlrFvXm8J84LMwGIw9q3U4u+Z9vFXlhB5x /languages/scss.min.js
sha384-Dy7I/j0yJlyliWiNrkNqXfxDrbN65q40s3JColgTYZQ7QJa7lcmK0WUL3i00/T51 /languages/sql.js
sha384-8q00eP+tyV9451aJYD5ML3ftuHKsGnDcezp7EXMEclDg1fZVSoj8O+3VyJTkXmWp /languages/sql.min.js
sha384-zoSc+TuKb10CxRmrZq/TRFkoAEM6ozSv3Cf8r50TxTx1r1Hcqaa5leVOEES2zauv /languages/stylus.js
sha384-Rd520i2dTJt7Zlfxu1YaFucV2Fd029x6Zczn9h0nD/AruF9OBK3UjS7wa0N5z9PI /languages/stylus.min.js
sha384-eq5Hd6gkTe5WGbF4XH+7WuiNnuq2zbdo/CV5idmTs5HIdlT6nsfGAJeb2aBqsRO6 /languages/vim.js
sha384-WcP1nsZR09ttNCYSUJGb4LmXw+/kA1O2iyojERHIrTB7Ou0ONLTsIkFOnFF2Umkj /languages/vim.min.js
sha384-tB5cwwsX4Ddp7P4d+ZInDb3nt4ihEEglHXoQ18eVLlT7soEn7bfGfABWKIn1l+H2 /languages/yaml.js
sha384-WC56y8OaFPt5Kj2HX6JAumxUYEjQmBDcSTJy2pn/N8g7dg1hKjeNVrJYoxlpeVmz /languages/yaml.min.js
sha384-fzsIYFvu8/NDQjABUiZM0J8lIz1V2kEo+qQ8RrT6L6CmKjQLqBmBIXzmd2q72BXu /highlight.js
sha384-Fu4CPfVw9kyU0IZw99l8jxiRgjK8ngIslbeQhNBod6EGDccLFor64BxD6usmT4CP /highlight.min.js
```

