-- Importing the std_logic library
library ieee;
use ieee.numeric_std.all;
use ieee.std_logic_1164.all;
use ieee.std_logic_UNSIGNED.all;

entity carry_zero_flag is
    port(
        alu_op  : in std_logic_vector(15 downto 0);
        zero_in : out std_logic;
        carry_in : in std_logic;

        -- Carry and Zero flag write enble;
        zero_en : in std_logic; 
        carry_en : in std_logic; 

        -- Carry and Zero flag
        zero_flag  : out std_logic;
        carry_flag : out std_logic;

        -- Clock
        clock : in std_logic;
        reset : in std_logic
    );
end entity carry_zero_flag;

architecture working of carry_zero_flag is
    
begin
    
    flag_update_process:process(clock,reset)
    begin
        if(alu_op = x"0000") then
            zero_in <= '1';
        else
            zero_in <= '0';
        end if;
        if reset = '1' then
            zero_flag <= '0';
            carry_flag <= '0';
        else
            if(falling_edge(clock)) then
                if(zero_en = '1') then
                    if(alu_op = x"0000") then
                        zero_flag <= '1';
                    else
                        zero_flag <= '0';
                    end if;
                end if;
                if(carry_en = '1') then
                    carry_flag <= carry_in;
                end if;
            end if;
        end if;
    end process flag_update_process;
end architecture working;
