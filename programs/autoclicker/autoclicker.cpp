#define WIN32_LEAN_AND_MEAN
#define _WIN32_WINNT 0x0500

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <string.h>
#include <windows.h>


#define X 123
#define Y 123
#define SCREEN_WIDTH 1024
#define SCREEN_HEIGHT 800


void MouseSetup(INPUT *buffer)
{
    buffer->type = INPUT_MOUSE;
    buffer->mi.dx = (0 * (0xFFFF / SCREEN_WIDTH));
    buffer->mi.dy = (0 * (0xFFFF / SCREEN_HEIGHT));
    buffer->mi.mouseData = 0;
    buffer->mi.dwFlags = MOUSEEVENTF_ABSOLUTE;
    buffer->mi.time = 0;
    buffer->mi.dwExtraInfo = 0;
}


void MouseMoveAbsolute(INPUT *buffer, int x, int y)
{
    buffer->mi.dx = (x * (0xFFFF / SCREEN_WIDTH));
    buffer->mi.dy = (y * (0xFFFF / SCREEN_HEIGHT));
    buffer->mi.dwFlags = (MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE);

    SendInput(1, buffer, sizeof(INPUT));
}


void MouseClick(INPUT *buffer)
{
    buffer->mi.dwFlags = (MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_LEFTDOWN);
    SendInput(1, buffer, sizeof(INPUT));

    Sleep(10);

    buffer->mi.dwFlags = (MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_LEFTUP);
    SendInput(1, buffer, sizeof(INPUT));
}


int main(int argc, char *argv[])
{
    INPUT buffer[1];

    MouseSetup(&buffer);

    MouseMoveAbsolute(&buffer, X, Y);
    MouseClick(&buffer);

    return 0;
