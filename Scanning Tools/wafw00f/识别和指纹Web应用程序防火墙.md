#  WAFW00F

WAFW00F identifies and fingerprints Web Application Firewall (WAF) products.

WAFW00F识别和指纹Web应用程序防火墙(WAF)产品。

## How does it work?

To do its magic, WAFW00F does the following:

为了施展其魔力，WAFW00F执行以下操作：

- Sends a _normal_ HTTP request and analyses the response; this identifies a
  number of WAF solutions.
  
  发送一个正常的HTTP请求并分析响应；这确定了一个
  
  waf解决方案的数目。
  
- If that is not successful, it sends a number of (potentially malicious) HTTP
  requests and uses simple logic to deduce which WAF it is.
  
  如果不成功，它会发送大量(可能是恶意的)HTTP请求，并使用简单的逻辑推断它是哪一个WAF。
  
- If that is also not successful, it analyses the responses previously
  returned and uses another simple algorithm to guess if a WAF or security
  solution is actively responding to our attacks.
  
  如果这也不成功，它会先分析回复
  
  返回并使用另一种简单的算法来猜测WAF或安全性
  
  解决方案正积极响应我们的攻击。

For further details, check out the source code on the main site,

有关详细信息，请查看主站点上的源代码，

[github.com/EnableSecurity/wafw00f](https://github.com/EnableSecurity/wafw00f).

## What does it detect?

It detects a number of WAFs. To view which WAFs it is able to detect run
WAFW00F with the `-l` option. At the time of writing the output is as follows:

它会检测到许多WAF。查看它能够检测到哪些WAF运行

带有`-l`选项的WAFW00F。在撰写本文时，输出如下：

    $ wafw00f -l
    
                                    ^     ^
            _   __  _   ____ _   __  _    _   ____
        ///7/ /.' \ / __////7/ /,' \ ,' \ / __/
        | V V // o // _/ | V V // 0 // 0 // _/
        |_n_,'/_n_//_/   |_n_,' \_,' \_,'/_/
                                    <
                                    ...'
    
        WAFW00F - Web Application Firewall Detection Tool
    
        By Sandro Gauci && Wendel G. Henrique
    
    Can test for these WAFs:
    
    Anquanbao
    FortiWeb
    NaxsiCisco ACE XML Gateway
    AWS WAF
    Citrix NetScaler
    Ergon Airlock
    F5 BIG-IP APM
    360WangZhanBao
    Mission Control Application Shield
    PowerCDN
    Safedog
    XLabs Security WAF
    Sucuri WAF
    F5 FirePass
    DenyALL WAF
    Trustwave ModSecurity
    CloudFlare
    Imperva SecureSphere
    Wallarm
    Incapsula WAF
    Radware AppWall
    F5 BIG-IP LTM
    Art of Defence HyperGuard
    Wordfence
    Aqtronix WebKnight
    Teros WAF
    eEye Digital Security SecureIIS
    BinarySec
    IBM DataPower
    Microsoft ISA Server
    NetContinuum
    NSFocus
    ChinaCache-CDN
    West263CDN
    F5 BIG-IP ASM
    AdNovum nevisProxy
    Barracuda Application Firewall
    Comodo WAF
    Profense
    BlockDoS
    Edgecast / Verizon Digital media
    Microsoft URLScan
    Applicure dotDefender
    USP Secure Entry Server
    DOSarrest
    F5 Trafficshield


## How do I use it?

First, install the tools as described [here](#how-do-i-install-it).

For help please make use of the `--help` option. The basic usage is to pass it
a URL as an argument. Example:

    $ wafw00f https://www.ibm.com/
    
                                     ^     ^
            _   __  _   ____ _   __  _    _   ____
           ///7/ /.' \ / __////7/ /,' \ ,' \ / __/
          | V V // o // _/ | V V // 0 // 0 // _/
          |_n_,'/_n_//_/   |_n_,' \_,' \_,'/_/
                                    <
                                     ...'
    
        WAFW00F - Web Application Firewall Detection Tool
    
        By Sandro Gauci && Wendel G. Henrique
    
    Checking https://www.ibm.com/
    The site https://www.ibm.com/ is behind Citrix NetScaler
    Number of requests: 6


## How do I install it?

The following should do the trick:

    python setup.py install

or

    pip install wafw00f

## Need a freelance pentester?

More information about the services that we offer at [Enable Security](http://enablesecurity.com/)

## How do I write my own new checks?

Follow the instructions on the [wiki](https://github.com/EnableSecurity/wafw00f/wiki/How-to-write-new-WAF-checks)

## Questions?

Contact [me](mailto:sandro@enablesecurity.com)

