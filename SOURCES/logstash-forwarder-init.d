#! /bin/sh

### BEGIN INIT INFO
# Provides:          logstash-forwarder
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Starts logstash-forwarder
# Description:       Logstash shipper
### END INIT INFO

[ -f /etc/rc.d/init.d/functions ] && . /etc/rc.d/init.d/functions

PATH=/sbin:/usr/sbin:/bin:/usr/bin
LOGSTASH_FORWARDER_BIN=/usr/bin/logstash-forwarder
LOGSTASH_FORWARDER_HOME=/var/lib/logstash-forwarder
LOGSTASH_FORWARDER_CONF=/etc/logstash-forwarder.conf
LOGSTASH_FORWARDER_OPTS='-spool-size 1024 -log-to-syslog'
PIDFILE=/var/run/logstash-forwarder.pid

RETVAL=0


start() {
    [ -x ${LOGSTASH_FORWARDER_BIN} ] || exit 5
    [ -f ${LOGSTASH_FORWARDER_CONF} ] || exit 6
    [ -d ${LOGSTASH_FORWARDER_HOME} ] || exit 7

    echo -n $"Starting logstash-forwarder: "

    daemon --pidfile $PIDFILE "cd $LOGSTASH_FORWARDER_HOME; $LOGSTASH_FORWARDER_BIN -config $LOGSTASH_FORWARDER_CONF $LOGSTASH_FORWARDER_OPTS >> /dev/null 2>&1 &"
    PID=`pidof logstash-forwarder`
    if [ -z $PID ]; then
        echo_failure
    else
        echo $PID > $PIDFILE
        echo_success
    fi

    echo
    return $retval
}

stop() {
    echo -n $"Stopping logstash-forwarder: "

    if [ -f $PIDFILE ]; then
        killproc -p $PIDFILE logstash-forwarder
        echo_success
        rm -f $PIDFILE
    else
        echo_failure
    fi

    echo
    return $retval
}

restart() {
    stop
    sleep 1
    start
}

status() {
    echo -n $"Checking logstash-forwarder: "

    if [ -f $PIDFILE ]; then
        PID=`cat $PIDFILE 2>/dev/null`
        if [ -z $PID ]; then
            echo "Process dead but pidfile exists"
        elif [ -z "`ps axf | grep ${PID} | grep -v grep`" ]; then
            echo "Process dead but pidfile exists"
        else
            echo "Running"
        fi
    else
        echo "Service not running"
    fi
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    status)
        status
        ;;
    *)
        echo "Usage: /etc/init.d/logstash-forwarder {start|stop|restart|status}" >&2
        exit 3
        ;;
esac
