#!/usr/bin/perl

# Julius��ǧ����̥����顢����ե�����(*.hyp)��������롣
# ���ץ���� -p �Ǥɤ���Υѥ��β���ե������������뤫���ꤹ�롣
# JNAS��
#
# ���: "-quiet" "-demo" ��Julius�¹Ի��ˤĤ�����硤���פ����������ʤ�
# ���Ȥ�����ޤ��ʽ��פ�ɬ�פ�ñ���N-gram�����ǥ������󤬽��Ϥ���ʤ������
#
# ����ˡ
# % nkf -e julius.log | \
#   perl mkhyp.pl \
#       -p {1|2} \
#   > julius.hyp

# ���ץ�������
require "getopts.pl";
&Getopts('hp:');

if ($opt_h || !$opt_p) {
    &usage;
}

if ($opt_p eq "1") {
    # ��1�ѥ��β���ñ��������������ݤ��Ѥ��롣
    $res = "pass1_best_wordseq";
}
elsif ($opt_p eq "2") {
    # ��2�ѥ��β���ñ��������������ݤ��Ѥ��롣
    $res = "wseq1";
}
else {
    &usage;
}

while (<>) {
    # �ե����ޥåȤ��줿id����Ϥ��롣
    if (/^input (MFCC |speech)file: (.*)$/) {
	($spkrid, $sentid) = &bunkai_id($2);
	$id = $spkrid . "-" . $sentid;
	print "$id\n";
    }

    # ǧ��ñ�������Ϥ��롣
    if (/^$res:\s+(.*)$/) {
	$sentence = $1;
	print "$sentence\n";
    }

    # CM ����Ϥ��� (03/06/11)
    if (/^cmscore1:\s+(.*)$/) {
	$cmscore = $1;
	print "cmscore: $cmscore\n";
    }
    if (/^cmscore1\[(.*)\]:\s+(.*)$/) {
	$cmalpha = $1;
	$cmscore = $2;
	print "cmscore[$cmalpha]: $cmscore\n";
    }

}

sub usage {
    print "nkf -e julius_log | ";
    print "jperl -Leuc mkhyp.pl <OPTS> > hypothesis_file\n";
    print "  OPTS --> [-h] -p {1|2}\n";
    print "    -h       --> show help\n";
    print "    -p {1|2} --> select 1pass or 2pass\n";
    exit(-1);
}

sub bunkai_id {
    local($fpath) = @_;
    $fpath =~ s/^.*\///;
    $fpath =~ m/^([^0-9]+[0-9]{3})([0-9]{3})/;
    ($1, $2);
}
