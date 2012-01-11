#!/bin/bash
###################################
#
#       check-nrpe-wrapper.sh
#
#		wrapper for check_nrpe plugin 
#		to handle optional arguments
#		
###################################

HOST=$1;
SSL=$2;
XFLAGS=$3;
PLUGIN=$4;
XARGS=$5;


COMMAND="$ZENHOME/libexec/check_nrpe"

if [ "$HOST" ] ; then
	COMMAND=$COMMAND" -H "$HOST
fi

if [ "$SSL" == "False" ] ; then
	COMMAND=$COMMAND" -n"
fi

if [ "$XFLAGS" ] ; then
	COMMAND=$COMMAND" "$XFLAGS
fi

if [ "$PLUGIN" ] ; then
	COMMAND=$COMMAND" -c "$PLUGIN
fi

if [ "$PASS" ] ; then
	COMMAND=$COMMAND":"$PASS
fi

if [ "$XARGS" ] ; then
        COMMAND=$COMMAND" -a "
        #FXARGS=$(echo $XARGS | sed -e 's/\\n/|/g')
        IFS_BAK=$IFS
        #IFS='|'
	IFS=$'\n'
        for ARG in ${XARGS}; do
                COMMAND=$COMMAND' "'$ARG'"'
        done
        IFS=$IFS_BAK
fi



/bin/sh -c "$COMMAND"


