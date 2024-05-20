package com.codingrecipe.member.controller;

import com.codingrecipe.member.dto.MemberDTO;
import com.codingrecipe.member.service.MemberService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpSession;
import java.util.Date;
import java.util.List;

@Controller
@RequestMapping("/member")
@RequiredArgsConstructor
public class MemberController {
    private final MemberService memberService;

//    @GetMapping("/member/save") // /member/member/save
    @GetMapping("/save")
    public String saveForm() {
        return "save";
    }

    @PostMapping("/save")
    public String save(@ModelAttribute MemberDTO memberDTO, HttpSession session, Model model) {
        memberDTO.setSignDate(new Date());
        String checkResult = memberService.emailCheck(memberDTO.getMemberEmail());
        if (checkResult.equals("ok")) {
            // 중복되지 않은 경우에만 회원가입 처리
            int saveResult = memberService.save(memberDTO);
            if (saveResult > 0) {
                return "login"; // 회원가입 성공 시 로그인 페이지로 이동
            } else {
                model.addAttribute("error", "회원가입에 실패했습니다. 다시 시도해주세요.");
                return "save"; // 회원가입 실패 시 회원가입 페이지로 이동
            }
        } else {
            model.addAttribute("error", "중복된 이메일 주소입니다. 다른 이메일 주소를 입력해주세요.");
            return "save"; // 중복된 이메일 주소일 경우 회원가입 페이지로 이동
        }
    }

    @GetMapping("/login")
    public String loginForm() {
        return "login";
    }

    @PostMapping("/login")
    public String login(@ModelAttribute MemberDTO memberDTO,
                        HttpSession session) {
        boolean loginResult = memberService.login(memberDTO);
        if (loginResult) {
            session.setAttribute("loginEmail", memberDTO.getMemberEmail());
            return "main";
        } else {
            return "login";
        }

    }

    @GetMapping("/")
    public String findAll(Model model) {
        List<MemberDTO> memberDTOList = memberService.findAll();
        model.addAttribute("memberList", memberDTOList);
        return "list";
    }

    // /member?id=1
    @GetMapping
    public String findById(@RequestParam("id") Long id, Model model) {
        MemberDTO memberDTO = memberService.findById(id);
        model.addAttribute("member", memberDTO);
        return "detail";
    }

    @GetMapping("/my-info") // 내정보 페이지로 이동하는 매핑
    public String getMyInfo(HttpSession session, Model model) {
        // 세션에서 로그인한 사용자의 이메일 가져오기
        String loginEmail = (String) session.getAttribute("loginEmail");
        // 이메일을 기반으로 현재 로그인한 사용자의 정보를 가져옴
        MemberDTO memberDTO = memberService.findByMemberEmail(loginEmail);
        // 모델에 사용자 정보를 담아서 detail.jsp로 전달
        model.addAttribute("member", memberDTO);
        return "detail"; // detail.jsp로 이동
    }

    @GetMapping("/delete")
    public String delete(@RequestParam("id") Long id) {
        memberService.delete(id);
        return "redirect:/member/";
    }

    // 수정화면 요청
    @GetMapping("/update")
    public String updateForm(HttpSession session, Model model) {
        // 세션에 저장된 나의 이메일 가져오기
        String loginEmail = (String) session.getAttribute("loginEmail");
        MemberDTO memberDTO = memberService.findByMemberEmail(loginEmail);
        model.addAttribute("member", memberDTO);
        return "update";
    }

    // 수정 처리
    @PostMapping("/update")
    public String update(@ModelAttribute MemberDTO memberDTO) {
        boolean result = memberService.update(memberDTO);
        if (result) {
            return "redirect:/member?id=" + memberDTO.getId();
        } else {
            return "index";
        }
    }

    @PostMapping("/email-check")
    public @ResponseBody String emailCheck(@RequestParam("memberEmail") String memberEmail) {
        System.out.println("memberEmail = " + memberEmail);
        String checkResult = memberService.emailCheck(memberEmail);
        return checkResult;
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        // 세션에서 로그인 정보 삭제
        session.removeAttribute("loginEmail");
        // 로그아웃 후 리다이렉트할 페이지로 이동
        return "index";
    }
}













