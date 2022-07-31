module patternMoorev(
    input logic clk,
    input logic reset,
    input logic a,
    output logic y);
    parameter [1:0] S0, S1, S2;
    reg state, nextstate;
    // state register
    always @(posedge clk, posedge reset)
    begin
        if (reset) state <= S0;
        else state <= nextstate;
        // next state logic
        begin
            case (state)
            S0: if (a) nextstate = S0;
            else nextstate = S1;
            S1: if (a) nextstate = S2;
            else nextstate = S1;
            S2: if (a) nextstate = S0;
            else nextstate = S1;
            default: nextstate = S0;
            endcase
        end
    end
    // output logic
    assign y = (state = = S2);
endmodule