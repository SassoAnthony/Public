%
% Mid-term Project
% Tic-Tac-Toe
% By Anthony Sasso.
% 10/12/2021
%

-module(ttt).
-author('Anthony Sasso').
-define(else, true).
-export([start/0, game/2]).
%-export([printBoard/1, printRow/1]).
%-export([getVictoryMove/2]).

%
% -- Public --
%

start() ->
    io:fwrite("~nLet's play Tic-Tac-Toe!~n"),
    io:fwrite("You will be playing against the computer.~n"),
    io:fwrite("The game board will look like this: ~n~n"),
    io:fwrite(" 1 | 2 | 3 ~n"),
    io:fwrite("---|---|---~n"),
    io:fwrite(" 4 | 5 | 6 ~n"),
    io:fwrite("---|---|---~n"),
    io:fwrite(" 7 | 8 | 9 ~n~n"),
    Board = [1, 2, 3, 4, 5, 6, 7, 8, 9],
    io:fwrite("You will use the values (1-9) to play.~n~n"),
    io:fwrite("Here is the starting board: ~n"),
    printBoard(Board),
    game(Board, 1).

game(Board, TurnCounter) -> 
    if (TurnCounter == 5) ->
        % Check for ties
        PlayerWinPos1 = getVictoryMove(Board, 'X'),
        ComputerWinPos1 = getVictoryMove(Board, 'O'),
        if ((PlayerWinPos1 == 0) and (ComputerWinPos1 == 0)) ->
            Tie1 = true;
        ?else ->
            Tie1 = false
        end;
    ?else ->
        Tie1 = false
    end,
    if (Tie1 == false) ->
        NewBoard = playerTurn(Board),
        printBoard(NewBoard);
    ?else ->
        NewBoard = Board
    end,
    Winner1 = checkOutcome(NewBoard),
    if (Winner1 == none) ->
        if (TurnCounter == 4) ->
            % Check for ties
            PlayerWinPos2 = getVictoryMove(NewBoard, 'X'),
            ComputerWinPos2 = getVictoryMove(NewBoard, 'O'),
            if ((PlayerWinPos2 == 0) and (ComputerWinPos2 == 0)) ->
                Tie2 = true;
            ?else ->
                Tie2 = false
            end;
        ?else ->
            Tie2 = false
        end,
        if ((TurnCounter < 5) and (Tie2 == false)) ->
            NewerBoard = computerTurn(TurnCounter, NewBoard, NewBoard),
            printBoard(NewerBoard),
            Winner2 = checkOutcome(NewerBoard),
            if (Winner2 == none) ->
                game(NewerBoard, TurnCounter+1);
            ?else ->
                Winner2
            end;
        ?else ->
            'It is a tie.'
        end;
    ?else ->
        Winner1
    end.

%
% -- Private --
%

%
% -- Algorithm for computer moves --
%

% Turn 1: Take Center if possible
computerTurn(1, [_, _, _, _, 5, _, _, _, _], Board) -> computerMove(Board, 5);
% Turn 2: If computer has center and player has opposite corners, play an edge
computerTurn(2, ['X', _, _, _, 'O', _, _, _, 'X'], Board) -> computerMove(Board, 2);
computerTurn(2, [_, _, 'X', _, 'O', _, 'X', _, _], Board) -> computerMove(Board, 2);
% Turn 2: If computer has center and player has adjacent edges, play the corner between
computerTurn(2, [_, 'X', _, 'X', 'O', _, _, _, _], Board) -> computerMove(Board, 1);
computerTurn(2, [_, 'X', _, _, 'O', 'X', _, _, _], Board) -> computerMove(Board, 3);
computerTurn(2, [_, _, _, 'X', 'O', _, _, 'X', _], Board) -> computerMove(Board, 7);
computerTurn(2, [_, _, _, _, 'O', 'X', _, 'X', _], Board) -> computerMove(Board, 9);
% Turn 2: Other cases because algorithm im not sure exactly
computerTurn(2, ['X', _, _, _, 'O', _, _, 'X', _], Board) -> computerMove(Board, 7);
computerTurn(2, [_, _, 'X', _, 'O', _, _, 'X', _], Board) -> computerMove(Board, 9);
computerTurn(2, [_, _, _, _, 'O', 'X', 'X', _, _], Board) -> computerMove(Board, 9);

% Turn 1: Center is taken, take upper left corner
computerTurn(1, [_, _, _, _, 'X', _, _, _, _], Board) -> computerMove(Board, 1);
% Turn 2: If player has center and plays bottom right corner, play top right corner
computerTurn(2, [_, _, _, _, 'X', _, _, _, 'X'], Board) -> computerMove(Board, 3);

% Turn 2: If computer has center and player has no special matches, try to win
% Turn 2: If player has center and no special matches, try to win
% Turn 3+: Check for winning moves and make, otherwise try to win
computerTurn(_, [_, _, _, _, _, _, _, _, _], Board) ->
    ComputerWinningMove = getVictoryMove(Board, 'O'),
    PlayerWinningMove = getVictoryMove(Board, 'X'), 
    if  (ComputerWinningMove =/= 0) ->
            computerMove(Board, ComputerWinningMove);
        (PlayerWinningMove =/= 0) ->
            computerMove(Board, PlayerWinningMove);
        ?else ->
            Move = getMove(Board),
            computerMove(Board, Move)
    end.

% Gets a possible move for the computer
getMove([1, _, _, _, _, _, _, _, _]) -> 1;
getMove([_, 2, _, _, _, _, _, _, _]) -> 2;
getMove([_, _, 3, _, _, _, _, _, _]) -> 3;
getMove([_, _, _, 4, _, _, _, _, _]) -> 4;
getMove([_, _, _, _, 5, _, _, _, _]) -> 5;
getMove([_, _, _, _, _, 6, _, _, _]) -> 6;
getMove([_, _, _, _, _, _, 7, _, _]) -> 7;
getMove([_, _, _, _, _, _, _, 8, _]) -> 8;
getMove([_, _, _, _, _, _, _, _, 9]) -> 9.

% Detect victory moves, 0 = no move, # = position of winning move
% This algorithm is also used to check for ties
getVictoryMove([X, X, 3, _, _, _, _, _, _], X) -> 3;
getVictoryMove([X, 2, X, _, _, _, _, _, _], X) -> 2;
getVictoryMove([1, X, X, _, _, _, _, _, _], X) -> 1;
getVictoryMove([_, _, _, X, X, 6, _, _, _], X) -> 6;
getVictoryMove([_, _, _, X, 5, X, _, _, _], X) -> 5;
getVictoryMove([_, _, _, 4, X, X, _, _, _], X) -> 4;
getVictoryMove([_, _, _, _, _, _, X, X, 9], X) -> 9;
getVictoryMove([_, _, _, _, _, _, X, 8, X], X) -> 8;
getVictoryMove([_, _, _, _, _, _, 7, X, X], X) -> 7;
getVictoryMove([X, _, _, X, _, _, 7, _, _], X) -> 7;
getVictoryMove([X, _, _, 4, _, _, X, _, _], X) -> 4;
getVictoryMove([1, _, _, X, _, _, X, _, _], X) -> 1;
getVictoryMove([_, X, _, _, X, _, _, 8, _], X) -> 8;
getVictoryMove([_, X, _, _, 5, _, _, X, _], X) -> 5;
getVictoryMove([_, 2, _, _, X, _, _, X, _], X) -> 2;
getVictoryMove([_, _, X, _, _, X, _, _, 9], X) -> 9;
getVictoryMove([_, _, X, _, _, 6, _, _, X], X) -> 6;
getVictoryMove([_, _, 3, _, _, X, _, _, X], X) -> 3;
getVictoryMove([X, _, _, _, X, _, _, _, 9], X) -> 9;
getVictoryMove([X, _, _, _, 5, _, _, _, X], X) -> 5;
getVictoryMove([1, _, _, _, X, _, _, _, X], X) -> 1;
getVictoryMove([_, _, X, _, X, _, 7, _, _], X) -> 7;
getVictoryMove([_, _, X, _, 5, _, X, _, _], X) -> 5;
getVictoryMove([_, _, 3, _, X, _, X, _, _], X) -> 3;
getVictoryMove(_, _) -> 0.

% Check to see if anyone has won the game
checkOutcome([X, X, X, _, _, _, _, _, _]) -> announceWinner(X);
checkOutcome([_, _, _, X, X, X, _, _, _]) -> announceWinner(X);
checkOutcome([_, _, _, _, _, _, X, X, X]) -> announceWinner(X);
checkOutcome([X, _, _, X, _, _, X, _, _]) -> announceWinner(X);
checkOutcome([_, X, _, _, X, _, _, X, _]) -> announceWinner(X);
checkOutcome([_, _, X, _, _, X, _, _, X]) -> announceWinner(X);
checkOutcome([X, _, _, _, X, _, _, _, X]) -> announceWinner(X);
checkOutcome([_, _, X, _, X, _, X, _, _]) -> announceWinner(X);
checkOutcome(_) -> none.

announceWinner(X) ->
    if  (X == 'O') -> 'You lost. Better luck next time!';
        (X == 'X') -> 'You won! HOW???';
        ?else -> 'This should never happen'
    end.

computerMove(Board, Position) ->
    io:fwrite("Your opponent played \'O\' on position ~w.~n", [Position]),
    setSpace(Board, Position, 'O').

playerTurn(Board) ->
    case io:fread("Where would you like to play? ", "~d") of
        {ok, Input} ->  
            [Int] = Input,
            CanMove = canMove(Board, Int),
            if ((Int >= 1) and (Int =< 9)and CanMove) ->
                io:fwrite("You played \'X\' on position ~w.~n", Input),
                setSpace(Board, Int, 'X');
            ?else ->
                io:fwrite("Please enter a valid empty position.~n"),
                playerTurn(Board)
            end;
        {error, {fread,integer}} ->
            io:fwrite("Please enter a valid move (1-9).~n"),
            playerTurn(Board)
    end.

canMove([], _) ->
    false;
canMove(Board, Position) ->
    if (hd(Board) == Position) ->
        true;
    ?else ->
        canMove(tl(Board), Position)
    end.

setSpace(Board, Position, Value) -> 
    lists:map(fun(Item) -> if (Item == Position) -> Value; ?else -> Item end end, Board).

printBoard([]) -> io:fwrite("~n");
printBoard(Board) ->
    if (length(Board) =/= 9) ->
        io:fwrite("---|---|---~n");
    ?else ->
        nothing
    end,
    printRow([hd(Board), hd(tl(Board)), hd(tl(tl(Board)))]),
    io:fwrite("~n"),
    printBoard(tl(tl(tl(Board)))). 

printRow([]) -> nothing;
printRow(Board) ->
    if (length(Board) rem 3 =/= 0) ->
        io:fwrite("|");
    ?else ->
        nothing
    end,
    if (is_integer(hd(Board))) ->
        io:fwrite("   ");
    ?else ->
        io:fwrite("~w", [hd(Board)])
    end,
    printRow(tl(Board)).