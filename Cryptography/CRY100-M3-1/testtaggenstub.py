

import hmac


def gen_tag(msg, key):
    hm = hmac.new(key.encode(), digestmod="md5")
    hm.update(msg.encode())
    return hm.hexdigest()


if __name__ == '__main__':

    keyfilename = 'c:/users/ursos/desktop/school/thonnyprogs/cryptography/cry100-m3-1/master.key'
    datafilename = 'c:/users/ursos/desktop/school/thonnyprogs/cryptography/cry100-m3-1/tags.txt'

    with open(keyfilename) as f:
        key = f.read()

    with open(datafilename) as g:
        data = g.readlines()


    line_inc = 0
    for line in data:
        stripped = line.strip("\n")
        line_inc += 1
        sentence, supplied_hmac = stripped.split(":")
        h_mac = gen_tag(sentence, key)

        if h_mac != supplied_hmac:
            conflict_hmacs = open("c:/users/ursos/desktop/school/thonnyprogs/cryptography/cry100-m3-1/hmac_conflicts.txt", "a")
            output = f'\nConflicting HMACs:\nLine {line_inc}: {sentence}\n------> tags.txt HMAC: {supplied_hmac} vs. Actual HMAC: {h_mac}\n'
            print(output)
            conflict_hmacs.write(output)

    conflict_hmacs.close() 
    f.close()
    g.close()
