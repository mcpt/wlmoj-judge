#define _DEFAULT_SOURCE
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/syscall.h>
#include <unistd.h>

int main() {
    int fd;
    if ((fd = syscall(SYS_open, NULL, O_RDONLY)) >= 0) {
        close(fd);
        puts("Should not open the file");
    } else if (errno == EFAULT) {
        puts("Hello, World!");
    } else {
        printf("Wrong errno: %d", errno);
    }
}
