#! /bin/sh

# julius -C julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/main.jconf > /dev/null &
# julius -C ./julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/main.jconf -C ./julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/am-gmm.jconf -module > /dev/null &
# julius -C ./dictation-kit-v4.3.1-linux/main.jconf -C ./dictation-kit-v4.3.1-linux/am-gmm.jconf -module > /dev/null &

# julius -C ./julius-4.4.2/julius-kit/grammar-kit-4.3.1/hmm_mono.jconf -C ./julius-4.4.2/julius-kit/grammar-kit-4.3.1/hmm_ptm.jconf -module > /dev/null &
julius -C ./dictation-kit-v4.3.1-linux/am-gmm.jconf -nostrip -gram ./dict/greeting -input mic -module > /dev/null & 

echo $!
sleep 2
