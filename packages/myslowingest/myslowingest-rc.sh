#!/bin/bash
#
# myslowingest
#
# chkconfig: 2345 98 02
# description: Starts and stops a single myslowingest instance on this system
#

### BEGIN INIT INFO
# Provides:          myslowingest
# Required-Start:    $local_fs $network $syslog
# Required-Stop:     $local_fs $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: MySQL slowlog ingestor.
# Description: MySQL slowlog ingestor.
### END INIT INFO



PATH=/usr/bin:/sbin:/bin:/usr/sbin
export PATH

[ -f /etc/sysconfig/myslowingest ] && . /etc/sysconfig/myslowingest
pidfile=${PIDFILE-/var/run/myslowingest/myslowingest.pid}
binfile="/usr/bin/myslowingest"
datadir=${DATADIR-/var/lib/mysql/slowlog}
args="-d -D $datadir -P $pidfile"
slowlog_user="${SLOWLOG_USER:-mysql}"
wrapper="su"
wrapperopts="$slowlog_user -c"
RETVAL=0

# Source function library.
. /etc/rc.d/init.d/functions

# Determine if we can use the -p option to daemon, killproc, and status.
# RHEL < 5 can't.
if status | grep -q -- '-p' 2>/dev/null; then
    daemonopts="--pidfile $pidfile"
    pidopts="-p $pidfile"
fi

if command -v runuser >/dev/null 2>&1; then
    wrapper="runuser"
fi

start() {
    echo -n $"Starting myslowingest: "
    install -o $slowlog_user -g $slowlog_user -d "$datadir" "/var/run/myslowingest"
    if [ $? -ne 0 ]; then
        echo
        exit 1
    fi
    daemon $daemonopts $wrapper $wrapperopts \"$binfile $args\"
    RETVAL=$?
    echo
    return $RETVAL
}

stop() {
    echo -n $"Stopping myslowingest: "
    killproc $pidopts $binfile
    RETVAL=$?
    echo
    [ $RETVAL = 0 ] && rm -f ${pidfile}
}

restart() {
    if [ $? -ne 0 ]; then
        return 1
    fi
    stop
    start
}

rh_status() {
    status $pidopts $binfile
    RETVAL=$?
    return $RETVAL
}

rh_status_q() {
    rh_status >/dev/null 2>&1
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
    condrestart|try-restart)
        rh_status_q || exit 0
        restart
    ;;
    status)
        rh_status
    ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart|condrestart}"
        exit 1
esac

exit $RETVAL
