package MeasureTflinear;

use strict;
use warnings;
use MeasureTf;

use vars qw(@ISA);
@ISA = qw(MeasureTf);

#--------------------------------------------------
# Construtor
#-------------------------------------------------- 
sub new {
    my $proto = shift;
    my $class = ref($proto) || $proto;
    my $self  = $class->SUPER::new(@_);
    
    bless $self, $class;
    
    $self->{measureName} = "TF-Linear";
    $self->{smooth}      = "enabled";
    $self->{type}        = "float";
    $self->{fixed}       = "false";

    return $self;
}

#--------------------------------------------------
# Funcao que retorna o valor da medida desejada
# para um determinado nome
# Parametro 0 = Nome
#-------------------------------------------------- 
sub getValue {
    my $self  = shift;
    my $names = $_[0];
    
    $names->setAux(1-($names->getCount()/$self->{nFiles}));
}

#--------------------------------------------------
# Funcao que retorna o valor do Smooth para quando
# a medida � igual a zero
# Parametro 0 = Nome
#-------------------------------------------------- 
sub getSmooth {
    my $self  = shift;
    my $names = $_[0];

    $names->setAux(1-($names->getCount()/($self->{nFiles}*1.2)));
}

1;
