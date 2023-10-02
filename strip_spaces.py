# Strip every space from a paragraph or sentence

file = '''anubis, baidu, bevigil, binaryedge, bing, bingapi, bufferoverun, brave,
censys, certspotter, criminalip, crtsh, dnsdumpster, duckduckgo, fullhunt,
github-code, hackertarget, hunter, hunterhow, intelx, netlas, onyphe, otx,
pentesttools, projectdiscovery, rapiddns, rocketreach, securityTrails,
sitedossier, subdomaincenter, subdomainfinderc99, threatminer, tomba,
urlscan, virustotal, yahoo, zoomeye
'''



def remove_spaces_with_replace(paragraph):
    return paragraph.replace(" ", "")


result = remove_spaces_with_replace(file)
print(result)
